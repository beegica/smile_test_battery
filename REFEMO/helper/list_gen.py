#RefEmo: List Generation
#Paul Cheng
#

# DATA STRUCTURES
#
# 
# blocks - list of dictionaries. Each element is a dictionary 
#   with the following keys:
#       'refresh_trials' - list of dictionaries, each containing data 
#                          for a single refresh trial. Keys are:
#               'block'         - block number as an integer (0 = practice block)
#               'trial'         - trial number within the block
#               'valences'      - 'pos-neu', 'neg-neu', 'neu-neu'
#               'val_order'     - 'pos-neu', 'neu-pos', 'neg-neu', 'neu-neg', 'neu-neu'
#               'refresh_side'  - 'UP' or 'DOWN'
#               'val_refresh'   - 'pos', 'neg', 'neu'
#               'up_stim'     - WordDict for the up stimulus
#               'down_stim'    - WordDict for the down stimulus
#       'test_trials' - list of dictionaries, each containing data 
#                       for a single test trial. Keys are:
#               'block'         - block number as an integer (0 = practice block)
#               'refresh_trial'         - refresh trial number within the block
#               'test_pos'      - serial position within the test block
#               'item_type'     - 'TARGET' or 'LURE'
#               'valences'      - from the refresh trial ('NA' for lures)
#               'val_order'     - from the refresh trial ('NA' for lures)
#               'refresh_side'  - from the refresh trial ('NA' for lures)
#               'val_refresh'   - from the refresh trial ('NA' for lures)
#               'test_stim'     - WordDict for the tested stimulus
#               'other_stim'    - wordDict for the companion (non-tested) stimulus
#
# each stimulus is a WordDict with the following attributes (keys):
#       'name'      - name of stimulus 
#       'filepath'  - complete path to image file
#       'desc'      - 'HUMAN' or 'NONHUMAN'
#       'val_cat'   - valence category ('pos', 'neg', or 'neu')
#       'valmn'     - mean valence
#       'aromn'     - mean arousal
#       'to_be_refred' - Boolean value
#       'to_be_tested' - Boolean value   

# EXPERIMENT DESIGN NOTES
#
# trials per block = 14
#   4  +~  (+~ refresh L, +~ refresh R, ~+ refresh L, ~+ refresh R)
#   4  +~  (-~ refresh L, -~ refresh R, ~- refresh L, ~- refresh R)
#   2  ~~  (refresh L, refresh R)
#
# trials are randomized within blocks
# Num blocks = 8

import os
import random
import csv
import config
import copy
from random import shuffle

print config.val_range

def recarray_to_pool(words):
    """
    Create a new pool from a set of words defined in
    a record array
    """
    new_pool = []
    for row in words:
        #print row
        new_pool.append(dict(desc=str(row['Description']),
                            name=str(row['Description']),
                            valmn=float(row['Valence Mean']),
                            valsd=float(row['Valence SD']),
                            aromn=float(row['Arousal Mean']),
                            arosd=float(row['Arousal SD']),
                            dominmn=float(row['Dominance Mean']),
                            dominsd=float(row['Dominance SD']),
                            word_freq=row['Word Frequency']))

        
    return new_pool

def create_pools(config):
    """
    Load the stimulus pools. 
    Select from the wordpool using valence and arousal ranges in the
    config file.  
    """

    print "Loading word pools..."
    
    # Create an empty dictionary of pools
    pos= []
    neg = []
    neu = []    
    pools = dict()

    # load word_pool
    pd = csv.DictReader(open(config.poolFile,'rb'))
    words = [l for l in pd]
    new_pool= recarray_to_pool(words)

    
    # get the pos,neg,neu pools
    
    for i in new_pool:
    #print i
        if ((i['valmn'] >= config.val_range['pos'][0]) &
            (i['valmn'] <= config.val_range['pos'][1]) &
            (i['aromn'] >= config.aro_range['pos'][0]) &
            (i['aromn'] <= config.aro_range['pos'][1])):
                pos.append(i)
    pools['pos']= pos
    random.shuffle(pools['pos'])
    
    for i in new_pool:
    #print i
        if ((i['valmn'] >= config.val_range['neg'][0]) &
            (i['valmn'] <= config.val_range['neg'][1]) &
            (i['aromn'] >= config.aro_range['neg'][0]) &
            (i['aromn'] <= config.aro_range['neg'][1])):
                neg.append(i)

    pools['neg'] = neg
    random.shuffle(pools['neg'])

    #random.shuffle(self.neg_words)

    for i in new_pool:
    #print i
        if ((i['valmn'] >= config.val_range['neu'][0]) &
            (i['valmn'] <= config.val_range['neu'][1]) &
            (i['aromn'] >= config.aro_range['neu'][0]) &
            (i['aromn'] <= config.aro_range['neu'][1])):
                neu.append(i)
    
    #takeout the extreme valmn object
#    extreme_words = ['vagina', 'bereavement', 'nurse', 'bandage', 'neurotic', 
#    'dawn', 'naked', 'obey', 'plane', 'virtue', 'skeptical', 
#    'coarse', 'wife', 'virgin', 'moral', 'idol', 'lavish', 'nipple']
#    crazy = []
#    {'neg': (1.8, 3.63), 'neu': (4.52, 6.35), 'pos': (6.85, 8.34)}

    #print len(neu)
   
    #print len(neu)
   # x=[]
   #for i in range(len(neu)):
   #     print i
   # for i in range(len(neu)-1):
        
        #print i
    #    x.append(neu[i])
    
     #   for g in range(len(extreme_words)):
     #           if neu[i]['name'] == extreme_words[g]:
                #print neu[i]['name']
     #           cra = neu.pop(i)
     #           crazy.append(cra)
                #print crazy
     #           print len(crazy)
    
            
    #if len(crazy)== len(extreme_words):
    #    print "filter applied"
    #else:
   #     print "filter fail"

    pools['neu'] = neu
    random.shuffle(pools['neu'])
    
    


    #print pools
    print len(pools['pos'])
    print len(pools['neg'])
    print len(pools['neu'])
    
    

    # return the pools
    #print pools
    return pools

def create_block(config, pools, blocknum=0):
    """
    Generate a block containing stimuli for practice refresh, refresh, practice test and test trials.

    INPUT ARGS:
        config      - Configuration object
        pools       - dictionary of pools
        [block_num] - integer (default = 0)
    """

    print 'Creating block %d' % blocknum
    
    # Create an empty list of trials
    block = {'block_num':blocknum,
             'refresh_trials':[],
             'test_trials':[],
             'practice_trial':[],
             'practice_test_trial':[]}
      
    ################
    #Practice trial#
    ################
    if blocknum <= 1:  
             # Loop over the trials in the block composition definition
        for r in range(config.practice_block_reps):
            # Loop over the trial definitions for a block
            for t in range(len(config.prac_block_def)):
                
                vals, uval, dval, refside = config.prac_block_def[t]

                # Get up stimulus and set attributes
                ustim = pools[uval].pop()
#               ustim['filepath'] = os.path.abspath(os.path.join(config.image_pool, 
#                                                        ustim['name']+.jpg'))
                ustim['val_cat'] = uval.upper()
                if 'desce' not in ustim.keys():
                    ustim['desc']= 'empty'

                # Get down stimulus and set attributes
                dstim = pools[dval].pop()
                dstim['val_cat'] = dval.upper()
#               dstim['filepath']=  os.path.abspath(os.path.join(config.image_pool, 
#                                                        dstim['name']+.jpg'))
                if 'desce' not in ustim.keys():
                    dstim['desc']= 'empty'
                    
                    # Select the image to be refreshed and tested
                    if refside.upper() == 'UP':
                        val_refresh = ustim['val_cat']
                        ustim['to_be_refred'] = True
                        ustim['to_be_tested'] = True
                        dstim['to_be_refred'] = False
                        dstim['to_be_tested'] = False
                    else:
                        val_refresh = dstim['val_cat']
                        ustim['to_be_refred'] = False
                        ustim['to_be_tested'] = False
                        dstim['to_be_refred'] = True
                        dstim['to_be_tested'] = True
                            
                            # Assign the stimuli to a refresh trial
                block['practice_trial'].append({'block':blocknum,
                                                'trial':0, # will be set after shuffling
                                                'valences':vals,
                                                'val_order':'%s-%s' % (uval,dval),
                                                'refresh_side':refside.upper(),
                                                'val_refresh':val_refresh,
                                                'up_stim':ustim.copy(),
                                                'down_stim':dstim.copy(),
                                                'trial_type': 'practice',
                                                'audio_name':''})         
        # Shuffle the refresh trials
        shuffle(block['practice_trial'])
                                                
        # Number the refresh trials after shuffling
        for t in range(len(block['practice_trial'])):
        # Number the refresh block
            block['practice_trial'][t]['trial'] = t+1
            block['practice_trial'][t]['audio_name']= '%s_%s_P.wav'%(t+1,block['practice_trial'][t]['block'])   

                
            
            
    ####################
    #practice rec trial#
    ####################
         # Create practice test trials
        for t in range(len(block['practice_trial'])):
        # Get the test stim and non-test stim
            if block['practice_trial'][t]['refresh_side'] == 'UP':
                teststim = block['practice_trial'][t]['up_stim']
                otherstim = block['practice_trial'][t]['down_stim']
            else:
                teststim = block['practice_trial'][t]['down_stim']
                otherstim = block['practice_trial'][t]['up_stim']
#        print 'Test trial %d: TARGET-%s. Pool sizes: pos=%d, neg=%d, neu=%d' \
#                % (t+1,teststim['val_cat'],len(pools['pos']),len(pools['neg']),len(pools['neu']))
        # Create a test trial for the refreshed item
            block['practice_test_trial'].append({'block':blocknum,
                                                 'refresh_trial':t+1,
                                                 'test_pos':0, # will be set after shuffling
                                                 'item_type':'TARGET',
                                                 'valences':block['practice_trial'][t]['valences'],
                                                 'val_order':block['practice_trial'][t]['val_order'],
                                                 'refresh_side':block['practice_trial'][t]['refresh_side'],
                                                 'val_refresh':block['practice_trial'][t]['val_refresh'],
                                                 'test_stim':teststim.copy(),
                                                 'other_stim':otherstim.copy(),
                                                 'trial_type':block['practice_trial'][t]['trial_type'],
                                                 'correct_resp':config.test_resp_keys[0]})
    # Create a corresponding LURE test trial by getting
    # a lure from the same valence pool as the target
#        print 'Test trial %d: LURE-%s. Pool sizes: pos=%d, neg=%d, neu=%d' \
#                % (t+1,teststim['val_cat'],len(pools['pos']),len(pools['neg']),len(pools['neu']))
            lurestim = pools[teststim['val_cat'].lower()].pop()
    #lurestim['filepath'] = os.path.abspath(os.path.join(config.image_pool,
    #                                                    lurestim['name']+'.jpg'))
            lurestim['val_cat'] = teststim['val_cat']
            lurestim['desc'] = 'empty'
            lurestim['to_be_refred'] = False
            lurestim['to_be_tested'] = True
            block['practice_test_trial'].append({'block':blocknum,
                                         'refresh_trial':-1,
                                         'test_pos':0, # will be set after shuffling
                                         'item_type':'LURE',
                                         'valences':'na',
                                         'val_order':'na',
                                         'refresh_side':'na',
                                         'val_refresh':'na',
                                         'test_stim':lurestim.copy(),
                                         'other_stim':None,
                                         'trial_type':'practice',
                                         'correct_resp':config.test_resp_keys[1]})

        # Shuffle the test trials
        shuffle(block['practice_test_trial'])

        # Number the test trials
        for t in range(len(block['practice_test_trial'])):
            block['practice_test_trial'][t]['test_pos'] = t+1
             
       
    ##########################
    #create experiement block#
    ##########################   
        
    # Loop over the trials in the bock composition definition
    for r in range(config.block_reps):
        # Loop over the trial definitions for a block
        for t in range(len(config.block_def)):

            vals, uval, dval, refside = config.block_def[t]

            # Get up stimulus and set attributes
            ustim = pools[uval].pop()
#            ustim['filepath'] = os.path.abspath(os.path.join(config.image_pool, 
#                                                        ustim['name']+.jpg'))
            ustim['val_cat'] = uval.upper()
            if 'desce' not in ustim.keys():
                ustim['desc']= 'empty'

            # Get down stimulus and set attributes
            dstim = pools[dval].pop()
            dstim['val_cat'] = dval.upper()
#            dstim['filepath']=  os.path.abspath(os.path.join(config.image_pool, 
#                                                        dstim['name']+.jpg'))
            if 'desce' not in ustim.keys():
                dstim['desc']= 'empty'

            # Select the image to be refreshed and tested
            if refside.upper() == 'UP':
                val_refresh = ustim['val_cat']
                ustim['to_be_refred'] = True
                ustim['to_be_tested'] = True
                dstim['to_be_refred'] = False
                dstim['to_be_tested'] = False
            else:
                val_refresh = dstim['val_cat']
                ustim['to_be_refred'] = False
                ustim['to_be_tested'] = False
                dstim['to_be_refred'] = True
                dstim['to_be_tested'] = True

            # Assign the stimuli to a refresh trial
            block['refresh_trials'].append({'block':blocknum,
                                            'trial':0, # will be set after shuffling
                                            'valences':vals,
                                            'val_order':'%s-%s' % (uval,dval),
                                            'refresh_side':refside.upper(),
                                            'val_refresh':val_refresh,
                                            'up_stim':ustim.copy(),
                                            'down_stim':dstim.copy()})
    #print block['refresh_trials'][1]

    # Shuffle the refresh trials
    shuffle(block['refresh_trials'])

    # Number the refresh trials after shuffling
    for t in range(len(block['refresh_trials'])):
        # Number the refresh block
        block['refresh_trials'][t]['trial'] = t+1
        block['refresh_trials'][t]['audio_name']= '%s_%s.wav'%(t+1,block['refresh_trials'][t]['block'])

    # Create test trials
    for t in range(len(block['refresh_trials'])):
        # Get the test stim and non-test stim
        if block['refresh_trials'][t]['refresh_side'] == 'UP':
            teststim = block['refresh_trials'][t]['up_stim']
            otherstim = block['refresh_trials'][t]['down_stim']
        else:
            teststim = block['refresh_trials'][t]['down_stim']
            otherstim = block['refresh_trials'][t]['up_stim']
#        print 'Test trial %d: TARGET-%s. Pool sizes: pos=%d, neg=%d, neu=%d' \
#                % (t+1,teststim['val_cat'],len(pools['pos']),len(pools['neg']),len(pools['neu']))
        # Create a test trial for the refreshed item
        block['test_trials'].append({'block':blocknum,
                                     'refresh_trial':t+1,
                                     'test_pos':0, # will be set after shuffling
                                     'item_type':'TARGET',
                                     'valences':block['refresh_trials'][t]['valences'],
                                     'val_order':block['refresh_trials'][t]['val_order'],
                                     'refresh_side':block['refresh_trials'][t]['refresh_side'],
                                     'val_refresh':block['refresh_trials'][t]['val_refresh'],
                                     'test_stim':teststim.copy(),
                                     'other_stim':otherstim.copy(),
                                     'correct_resp':config.test_resp_keys[0]})
        # Create a corresponding LURE test trial by getting
        # a lure from the same valence pool as the target
#        print 'Test trial %d: LURE-%s. Pool sizes: pos=%d, neg=%d, neu=%d' \
#                % (t+1,teststim['val_cat'],len(pools['pos']),len(pools['neg']),len(pools['neu']))
        lurestim = pools[teststim['val_cat'].lower()].pop()
        #lurestim['filepath'] = os.path.abspath(os.path.join(config.image_pool,
        #                                                    lurestim['name']+'.jpg'))
        lurestim['val_cat'] = teststim['val_cat']
        lurestim['desc'] = 'empty'
        lurestim['to_be_refred'] = False
        lurestim['to_be_tested'] = True
        block['test_trials'].append({'block':blocknum,
                                     'refresh_trial':-1,
                                     'test_pos':0, # will be set after shuffling
                                     'item_type':'LURE',
                                     'valences':'na',
                                     'val_order':'na',
                                     'refresh_side':'na',
                                     'val_refresh':'na',
                                     'test_stim':lurestim.copy(),
                                     'other_stim':None,
                                     'correct_resp':config.test_resp_keys[1]})

    # Shuffle the test trials
    shuffle(block['test_trials'])

    # Number the test trials
    for t in range(len(block['test_trials'])):
        block['test_trials'][t]['test_pos'] = t+1

    # return the block
    return block


def gen_blocks(config):
    """
    Create refresh (study) and test blocks for the RefEmo experiment
    """
    # Load the stimuli
    pools = create_pools(config)
    
    # Create the blocks
    blocks = []  
    for b in range(config.NUM_BLOCKS):
        blocks.append(create_block(config, pools,b+1))

    # display the pool residual size
    print 'Pool residual: pos=%d, neg=%d, neu=%d' \
                % (len(pools['pos']),len(pools['neg']),len(pools['neu']))    
    
    #print blocks[0]['test_trials'][0]
    #for i in blocks[0]['test_trials']:
    #        print i['refresh_trial']
    #for i in blocks[0]['test_trials']:
    #        print i['item_type']
    #print blocks[0]['study_trials'][1]
    # return the blocks
    return blocks

#block = gen_blocks(config)    

#for b in block:
#   for t in b['refresh_trials']:
#       print t
#print refresh

#for b in block:
#   for t in b['practice_trial']['audio_name']:
#