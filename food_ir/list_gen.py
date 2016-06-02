import os
import sys
import random
import numpy as np
import config

# From pyepl.pool import Pool


# Even number of savory and sweet, vs. non-food

# Fields to keep
fields_to_keep = ['Image_No',
                  'Item_description_english',
                  'protein_100g',
                  'fat_100g',
                  'carbs_100g',
                  'kcal_100g',
                  'no_items_image',
                  'gramms_total',
                  'protein_total',
                  'fat_total',
                  'carbs_total',
                  'Kcal_total',
                  'red',
                  'green',
                  'blue',
                  'object size',
                  'intensity',
                  'sd',
                  'complexity',
                  'norm. Complexity',
                  'medianpower',
                  'Recognizability',
                  'Familiarity',
                  'Valence',
                  'Arousal',
                  'Complexity',
                  'Palatability',
                  'Craving',
                  'type',
                  'contents',
                  'taste',
                  'processing']


def gen_study_list(num_items, lag_range, num_tries=100):
    worked = False
    for n in xrange(num_tries):
        sys.stdout.write('.')
        sys.stdout.flush()

        # Place them
        list_inds = np.array([-1]*(num_items*2))

        for i in range(num_items):
            # Get possible indices
            poss_inds = np.nonzero(list_inds<0)[0]

            if len(poss_inds) < 2:
                break

            # Place first in first available slot
            ind0 = poss_inds[0]
            list_inds[ind0] = i

            # Work with remaining inds
            poss_inds = poss_inds[1:]
            poss_inds = np.intersect1d(np.arange(*lag_range)+ind0,
                                       poss_inds)

            if len(poss_inds) < 1:
                break

            # Pick and place
            ind1 = random.choice(poss_inds)
            list_inds[ind1] = i

        # If we are here
        if not np.any(list_inds < 0):
            worked = True
            break

    if not worked:
        raise RuntimeError("Failed to generate valid list.")

    return list_inds



def gen_blocks(config):

    # Load the pool info
    images = np.load(config.pool_file)

    # Get indicies for each type we need
    savory_ind = np.nonzero(images['taste']=='Savory')[0].tolist()
    sweet_ind = np.nonzero(images['taste']=='Sweet')[0].tolist()
    nonfood_ind = np.nonzero(images['type']=='Non-Food')[0].tolist()

    # Shuffle them
    random.shuffle(savory_ind)
    random.shuffle(sweet_ind)
    random.shuffle(nonfood_ind)

    # Calc num needed each block
    num_savory = config.list_len//4
    num_sweet = config.list_len//4
    num_nonfood = config.list_len//2

    # Generate the study and test blocks
    study_blocks = []
    test_blocks = []
    for b in range(config.num_blocks):
        # Get study and test items
        study_items = [savory_ind.pop() for i in range(num_savory)] + \
                      [sweet_ind.pop() for i in range(num_sweet)] + \
                      [nonfood_ind.pop() for i in range(num_nonfood)]
        if config.do_test:
            test_items = [savory_ind.pop() for i in range(num_savory)] + \
                         [sweet_ind.pop() for i in range(num_sweet)] + \
                         [nonfood_ind.pop() for i in range(num_nonfood)]
            test_items += study_items[:]

        # Shuffle the order
        random.shuffle(study_items)
        if config.do_test:
            random.shuffle(test_items)

        # Get the study list inds
        list_inds = gen_study_list(config.list_len,
                                   config.lag_range,
                                   num_tries=config.num_tries)

        # Loop and fill actual data
        study_block = []
        for i,ind in enumerate(list_inds):
            # Set the presentation number
            if i > 0 and ind in list_inds[:i]:
                pres_num = 2
            else:
                pres_num = 1

            stim_info = dict()
            for f in fields_to_keep:
                stim_info[f] = images[f][study_items[ind]]
            stim_info['filename'] = '%04d.jpg'%images['Image_No'][study_items[ind]]
            study_trial = dict(block_num=b,
                               trial_num=i,
                               trial_type='study',
                               condition='target',
                               pres_num=pres_num,
                               #stim=item['content'],
                               stim_info=stim_info,
                               stim_path = os.path.join(config.pool_dir,stim_info['filename']))

            # Append it
            study_block.append(study_trial)

        if config.do_test:
            # Loop and fill the test block
            test_block = []
            for i,ind in enumerate(test_items):
                # Set the cond
                if ind in study_items:
                    cond = 'target'
                else:
                    cond = 'lure'

                stim_info = dict()
                for f in fields_to_keep:
                    stim_info[f] = images[f][ind]
                stim_info['filename'] = '%04d.jpg'%images['Image_No'][ind]
                test_trial = dict(block_num=b,
                                  trial_num=i,
                                  trial_type='test',
                                  condition=cond,
                                  pres_num=pres_num,
                                  #stim=item['content'],
                                  stim_info=stim_info,
                                  stim_path = os.path.join(config.pool_dir,stim_info['filename']))

                # Append it
                test_block.append(test_trial)

        # Append the blocks
        study_blocks.append(study_block)
        if config.do_test:
            test_blocks.append(test_block)

    # Return the study and test blocks
    return study_blocks,test_blocks

