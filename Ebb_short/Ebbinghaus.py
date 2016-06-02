################################################################################
#
# Ebbinghaus.py
#
# This is a short (5-10 minutes) experiment replicated some of the basic
# elements of Ebbinghaus's famous self administered memory experiments. It gives
# a lists of CVC words(nonsense or normal words) repeatedly presented until the
# participant gets them correct twice, then moves on to a new list. After the
# study phase, it then repeat the same lists, to allow ' savings" to be
# computed.
#
#
################################################################################


# Global imports
import os
import config
from gen_stim import block_maker
from gen_stim import mad_man_shuffler
from smile.common import *
from smile.video import TextInput
from random import shuffle
from math import floor


# Call lis_gen create list
non_sen_cvs_block = block_maker(True, config)
normal_cvc_block = block_maker(False, config)

# Create an experiment
exp = Experiment()

# Choose Words Type
with Parallel():
    # Set the stimulus type
    inst = Label(text = "choose a stimulus",
                font_size = config.text_size,
                center_y = (exp.screen.height/2+ 65))

    # Present the opptions
    left = Label(text = "Press 'F' for Nonsense CVS, or Press 'J' for 3 Letter Words",
                 font_size = config.text_size,
                 center_y = (exp.screen.height/2))

with UntilDone():
    kps = KeyPress(keys = ['F','J'],
                   correct_resp = 'F')
    Debug(keypressed = kps.pressed,
         correct_resp = kps.correct)
    # If key press is true means run an experiment with Nonsense CVS


with If(kps.correct == True):
    exp.instruct = config.meaningless_intro
    exp.blocks = non_sen_cvs_block
with Else():
    exp.instruct = config.cvc_intro
    exp.blocks = normal_cvc_block


# Study Loop Set UP
init_int= Label(text = exp.instruct, text_size = (exp.screen.height,None),
                font_size = config.inst_front,
                halign= 'left',
                valign = 'middle')
with UntilDone():
    kp= KeyPress()

# Run the Loop of Blocks
with Loop(exp.blocks) as trial_block:
    exp.num_loop = 0 # to keep track how many loop
    exp.num_corr = 0 # tp keep track how many time it was correct
    # While the number correct is less than the number needed, run this loop
    with Loop(conditional=(exp.num_corr < config.num_corr_need)):
        exp.num_stim_corr = 0
        # Loop until it is correct twice
        # Present 3-2-1 Ready? sequence
        with Loop(config.number_loop) as nl:
            Present = Label(text = nl.current,
                            font_size = config.text_size,
                            duration = config.count_down_timing)

        Ready = Label(text = "Ready!",
                      font_size = config.text_size,
                      duration = config.count_down_timing)

        # Present all the words one by one
        with Loop(trial_block.current['list_words']) as word:
            WORD = Label(text = word.current,
                         font_size = config.text_size,
                         duration = config.stim_on_time)

        # Present recall option
        # Randomized the word orders
        exp.words = trial_block.current['list_words']
        exp.word_present = Ref(mad_man_shuffler, exp.words)
        Debug(current_word_list = trial_block.current['list_words'],
              Shuffle_word_list = exp.word_present)

        # Present all words and enter responds
        exp.l_n_index = []
        exp.E = []
        with Parallel() as pp:
            # Present All the words and some TextInput boxes
            with Loop(Ref(range,config.num_word_list)) as lp:
                with pp.insert() as pi:
                    pre_stim = Label(text= exp.word_present[lp.i],
                                     color = 'White',
                                     center_x = exp.screen.center_x - 7*(exp.screen.width/20)+ lp.i*4*(exp.screen.width/20) - Ref(floor,lp.i/4.)*16*(exp.screen.width/20),
                                     center_y = exp.screen.center_y + (exp.screen.height)/6- Ref(floor,lp.i/4.)*2*(exp.screen.height)/6,
                                     font_size = config.text_size)
                    Enter = TextInput(multiline = False,
                                      center_x = exp.screen.center_x - 5*(exp.screen.width/20)+ lp.i*4*(exp.screen.width/20)- Ref(floor,lp.i/4.)*16*(exp.screen.width/20),
                                      center_y = exp.screen.center_y + (exp.screen.height)/6- Ref(floor,lp.i/4.)*2*(exp.screen.height)/6,
                                      input_filter = 'int',
                                      font_size = config.text_size)
                exp.E += [pi.last]
            MouseCursor()

        with UntilDone():
            # Using ButtonPress() state to create A "done" box to exist the trial
            with ButtonPress() as bp:
                  Button(text= 'Done', color = 'BLUE', font_size = 35,center_x = exp.screen.center_x,
                         center_y= exp.screen.center_y - 3*(exp.screen.height)/8)
            with Loop(exp.E) as lpE:
                exp.l_n_index += [Ref(int,lpE.current.text)]
            Debug(list_number = exp.l_n_index)

        # Creating references to input items
        exp.list_num = []
        with Loop(exp.l_n_index) as lp2:
            exp.list_num += [lp2.current - 1]

        # Use Python Loop to loop over If() to eval the respond
        # make sure particpant type only numbers between 1-8(indexing between 0-7)
        exp.l_above_prem = 0
        with Loop(Ref(range, Ref(len,exp.list_num))) as lp3:
            with If((exp.list_num[lp3.i] > 7) & (exp.list_num[lp3.i] < 0)):
                exp.l_above_prem += 1

        # Only eval if input number is between 1-8
        with If(exp.l_above_prem == 0):
            with Loop(Ref(range, Ref(len,exp.list_num))) as lp4:
                with If(Ref.getitem(exp.word_present, lp4.i) == trial_block.current['list_words'][exp.list_num[lp4.i]]):
                    exp.num_stim_corr += 1

                Debug(number_stim_correct = exp.num_stim_corr,
                    ref_get = Ref.getitem(exp.word_present, lp4.i),
                    ref_cur_tri_list = trial_block.current['list_words'][exp.list_num[lp4.i]],
                    current_index_num = exp.list_num[lp4.i],
                    current_loop_num = lp4.i)


            # Check if there are enough correct_resp to be consider correct trial
            with If( exp.num_stim_corr == 8):
                exp.num_loop += 1
                exp.num_corr += 1
            with Else():
                exp.num_loop += 1
                exp.num_corr = 0


            # Feedback
            with Parallel():
                # Presented:   num_corr / 10 Correct
                Label(text = Ref(str,exp.num_stim_corr) + ' / 8 Correct', font_size = config.text_size, center_x = exp.screen.center_x)
            with UntilDone():
                Wait(config.isi)

            # log values
            # correct word order,current word order,participant word order, total time spend
            # number of try, current correct time, set a current value of correct time

            Log(name = 'init_study',
                block_num = trial_block.current['block_num'],
                current_word_list = trial_block.current['list_words'],
                Shuffle_word_list = exp.word_present,
                Respond_input = exp.list_num,
                correct_resp = exp.num_stim_corr,
                loop_num = exp.num_loop,
                correct_trial = exp.num_corr)

        with Else():
            exp.num_loop += 1
            exp.num_corr = 0
            Label(text = config.number_instr,
                  font_size = config.inst_front)
            with UntilDone():
                Wait(config.isi)

            Log(name = 'init_study_i',
                block_num = trial_block.current['block_num'],
                current_word_list = trial_block.current['list_words'],
                Shuffle_word_list = exp.word_present,
                loop_num = exp.num_loop,
                correct_trial = exp.num_corr)





########################
##Non-sense Test Phase##
########################
# if you have a Python loop inside your smile code, you may not use Subrutine
#Testing Loop Set UP
#present instruction
test_p_intr = Label(text = config.testing_phase_instruction, text_size = (exp.screen.height,None),
      font_size = config.inst_front,
      halign= 'left',
      valign = 'middle')

with UntilDone():
    KeyPress()


with Loop(non_sen_cvs_block) as trial_block:
    exp.num_loop = 0 # to keep track how many loop
    exp.num_corr = 0 # tp keep track how many time it was correct
    with Loop(conditional=(exp.num_corr != config.num_corr_need)):
        exp.num_stim_corr = 0
        ### loop until it is correct twice
        ## present 3-2-1 Ready? sequence
        with Loop(config.number_loop) as nl:
            Label(text = nl.current,
                  font_size = config.text_size,
                  duration = config.count_down_timing)

        Label(text = "Ready!",
              font_size = config.text_size,
              duration = config.count_down_timing)

        ## present all the words one by one
        with Loop(trial_block.current['list_words']) as word:
            Label(text = word.current,
                  font_size = config.text_size,
                  duration = config.stim_on_time)

        ## present recall option
        # randomized the word orders
        exp.words = trial_block.current['list_words']
        exp.word_present = Ref(mad_man_shuffler, exp.words)
        Debug(current_word_list = trial_block.current['list_words'],
              Shuffle_word_list = exp.word_present)

        # Present all words and enter responds
        exp.l_n_index = []
        exp.E = []
        with Parallel() as pp:
            # Present All the words and some TextInput boxes
            with Loop(Ref(range,config.num_word_list)) as lptl:
                with pp.insert() as pitl:
                    Label(text= exp.word_present[lptl.i],
                                     color = 'White',
                                     center_x = exp.screen.center_x - 7*(exp.screen.width/20)+ lptl.i*4*(exp.screen.width/20) - Ref(floor,lptl.i/4.)*16*(exp.screen.width/20),
                                     center_y = exp.screen.center_y + (exp.screen.height)/6- Ref(floor,lptl.i/4.)*2*(exp.screen.height)/6,
                                     font_size = config.text_size)
                    Enter = TextInput(multiline = False,
                                      center_x = exp.screen.center_x - 5*(exp.screen.width/20)+ lptl.i*4*(exp.screen.width/20)- Ref(floor,lptl.i/4.)*16*(exp.screen.width/20),
                                      center_y = exp.screen.center_y + (exp.screen.height)/6- Ref(floor,lptl.i/4.)*2*(exp.screen.height)/6,
                                      input_filter = 'int',
                                      font_size = config.text_size)
                exp.E += [pi.last]
            MouseCursor()

        with UntilDone():
            # Using ButtonPress() state to create A "done" box to exist the trial
            with ButtonPress() as bp:
                  Button(text= 'Done', color = 'BLUE', font_size = 35,center_x = exp.screen.center_x,
                         center_y= exp.screen.center_y - 3*(exp.screen.height)/8)
            with Loop(exp.E) as lpE:
                exp.l_n_index += [Ref(int,lpE.current.text)]
            Debug(list_number = exp.l_n_index)


        # Creating references to input items
        exp.list_num = []
        with Loop(exp.l_n_index) as lptl2:
            exp.list_num += [lptl2.current - 1]

        # Use Python Loop to loop over If() to eval the respond
        # Make sure particpant type only numbers between 1-8(indexing between 0-7)
        exp.l_above_prem = 0
        with Loop(Ref(range, Ref(len,exp.list_num))) as lptl3:
            with If((exp.list_num[lptl3.i] > 7) & (exp.list_num[lptl3.i] < 0)):
                exp.l_above_prem += 1

        # Only eval if input number is between 1-8
        with If(exp.l_above_prem == 0):
            with Loop(Ref(range, Ref(len,exp.list_num))) as lptl4:
                with If(Ref.getitem(exp.word_present, lptl4.i) == trial_block.current['list_words'][exp.list_num[lptl4.i]]):
                    exp.num_stim_corr += 1

                Debug(number_stim_correct = exp.num_stim_corr,
                    ref_get = Ref.getitem(exp.word_present, lptl4.i),
                    ref_cur_tri_list = trial_block.current['list_words'][exp.list_num[lptl4.i]],
                    current_index_num = exp.list_num[lptl4.i],
                    current_loop_num = lptl4.i)


            # Check if there are enough correct_resp to be consider correct trial
            with If( exp.num_stim_corr == 8):
                exp.num_loop += 1
                exp.num_corr += 1
            with Else():
                exp.num_loop += 1
                exp.num_corr = 0


            # Feedback
            with Parallel():
                # Presented:   num_corr / 10 Correct
                Label(text = Ref(str,exp.num_stim_corr) + ' / 8 Correct', font_size = config.text_size, center_x = exp.screen.center_x)
            with UntilDone():
                Wait(config.isi)


            # Log values
            # Correct word order,current word order,participant word order, total time spend
            # Number of try, current correct time, set a current value of correct time

            Log(name = 'test',
                current_word_list = trial_block.current['list_words'],
                block_num = trial_block.current['block_num'],
                Shuffle_word_list = exp.word_present,
                Respond_input = exp.list_num,
                correct_resp = exp.num_stim_corr,
                loop_num = exp.num_loop,
                correct_trial = exp.num_corr)

        with Else():
            exp.num_loop += 1
            exp.num_corr = 0
            Label(text = config.number_instr,
                  font_size = config.inst_front)
            with UntilDone():
                Wait(config.isi)

            Log(name = 'test_i',
                current_word_list = trial_block.current['list_words'],
                block_num = trial_block.current['block_num'],
                Shuffle_word_list = exp.word_present,
                loop_num = exp.num_loop,
                correct_trial = exp.num_corr)

#Thanks participant for particpating in the experiment
Label(text = config.deb, text_size = (exp.screen.height,None),
      font_size = config.inst_front,
      halign= 'center',
      valign = 'middle')

with UntilDone():
    kp= KeyPress()

exp.run()




##################
#Analizing Script#
##################
###########################
#Setting up for processing#
###########################
from smile.log import LogReader
##acessing log
study_log_stats=LogReader(filename = 'data/1005/log_init_study_0.slog')
test_log_stats=LogReader(filename = 'data/1005/log_test_0.slog')

#read_record() read a line in the slog dic. Also if this state is being loop over, it will
#list each dic in seq order
temp_S= study_log_stats.read_record()
temp_T= test_log_stats.read_record()

#an example of read record()
#print 'this is study_log: %s'%(temp_S)
#print 'this is test_log: %s'%(temp_T)

#print all the keys of log
#print temp_S.keys()
#print temp_T.keys()

#set the keys for later use
#since both Study and Test has the same keys just use one set of keys
keys_S = temp_S.keys()
keys_T = temp_T.keys()
#create a list of empty list to fit all the data in there
num_keys_S= len(keys_S)
list_keys_S = []
for k in range(num_keys_S):
    list_keys_S.append([])

num_keys_T= len(keys_T)
list_keys_T = []
for k in range(num_keys_T):
    list_keys_T.append([])

#A function to orgnize slog-smile dic to reg dic
def dic_org(dic,l_keys, keys,log_stats):
    reorg_dic = dict(zip(keys, l_keys))
    while dic != None:
        for name in keys:
            reorg_dic[name].append(dic[name])
        dic= log_stats.read_record()
    return reorg_dic

study_dic = dic_org(temp_S,list_keys_S, keys_S,study_log_stats )
test_dic = dic_org(temp_T,list_keys_T, keys_T,test_log_stats)



#Testing
#print "This is the Current number of trials inside Study_dic: %s"%len(study_dic['loop_num'])
#print "This is the Current number of trials inside Test_dic: %s"%len(test_dic['loop_num'])

#Rocking Processing!!!!!!

def anal_dic_gen(dic,config):
    anal_dic = {'resp_order':[],
                'resp_correct':[],
                'total_corr_item_pos':[int() for i in range(config.num_word_list)]}
    #indexing respond order / boleaging responds
    for word_order in range(len(dic['Respond_input'])):
        anal_dic['resp_order'].append([])
        anal_dic['resp_correct'].append([])
        for i in range(len(dic['Respond_input'][word_order])):
            anal_dic['resp_order'][word_order].append('')
            anal_dic['resp_correct'][word_order].append(bool())

    #asign resp_order for eval
    for l in range(len(dic['Shuffle_word_list'])):
        for i in range(len(dic['Shuffle_word_list'][l])):
            anal_dic['resp_order'][l][dic['Respond_input'][l][i]] = dic['Shuffle_word_list'][l][i]
            # dic of respond's order[word order][index'respond_input_number'] = dic of shuffle_words[l][i]

    #booleaning the responds,and set up positions of correct respond for eval
    for l in range(len(anal_dic['resp_correct'])):
        for i in range(len(anal_dic['resp_correct'][l])):

            if anal_dic['resp_order'][l][i] == dic['current_word_list'][l][i]:
                anal_dic['resp_correct'][l][i] = True
                #asign total correct items for all the incorrect items
                if dic['correct_trial'][l] == 0:
                    anal_dic['total_corr_item_pos'][i] += 1

            else:
                anal_dic['resp_correct'][l][i] = False
    #Get all the incorrect trials
    anal_dic['num_inc'] = 0

    for t in dic['correct_trial']:
        if t == 0:
            anal_dic['num_inc'] += 1

    return anal_dic
#generate analysis dic
anal_s_dic = anal_dic_gen(study_dic,config)
anal_t_dic = anal_dic_gen(test_dic,config)

#total number of incorrect trials
#total_number_s_trial_inc = len(anal_s_dic['resp_correct'])
#total_number_t_trial_inc = len(anal_t_dic['resp_correct'])
if anal_s_dic['num_inc'] > 0:
    pos_s = [floor(float(i)/float(anal_s_dic['num_inc'])*100) for i in anal_s_dic['total_corr_item_pos']]
if anal_t_dic['num_inc'] > 0:
    pos_t = [floor(float(i)/float(anal_t_dic['num_inc'])*100) for i in anal_t_dic['total_corr_item_pos']]

num_loop_s= []
for i in range(len(study_dic['correct_trial'])):
    if study_dic['correct_trial'][i] == 2:
        num_loop_s.append(study_dic['loop_num'][i])
learn_average_s = sum(num_loop_s)/len(num_loop_s)

num_loop_t= []
for i in range(len(test_dic['correct_trial'])):
    if test_dic['correct_trial'][i] == 2:
        num_loop_t.append(test_dic['loop_num'][i])
learn_average_t = sum(num_loop_t)/len(num_loop_t)

#list one serial corr
#[[0]/total_num_stim[0], trials_corr[1]/total_num_stim[1].....etc]
#study
ser_corr_s=[[]for i in range(config.num_block)]
for t in study_dic['correct_resp'][:num_loop_s[0]]:
    ser_corr_s[0].append(float(t)/float(config.num_word_list))
for t in study_dic['correct_resp'][num_loop_s[0]:]:
    ser_corr_s[1].append(float(t)/float(config.num_word_list))
#test
ser_corr_t=[[]for i in range(config.num_block)]
for t in test_dic['correct_resp'][:num_loop_t[0]]:
    ser_corr_t[0].append(float(t)/float(config.num_word_list))
for t in test_dic['correct_resp'][num_loop_t[0]:]:
    ser_corr_t[1].append(float(t)/float(config.num_word_list))



print 'Total number of times to learn List 1 during study: %s'%num_loop_s[0]
print 'Total number of times to learn List 2 during study: %s'%num_loop_s[1]
print 'average loop to learn during study:%s' %learn_average_s
print 'Total number of times to learn List 1 during test: %s'%num_loop_t[0]
print 'Total number of times to learn List 2 during test: %s'%num_loop_t[1]
print 'average loop to learn during test:%s' %learn_average_t
print 'List 1 trials recall rate during study: %s'%ser_corr_s[0]
print 'List 2 trials recall rate during study: %s'%ser_corr_s[1]
print 'List 1 trials recall rate during test: %s'%ser_corr_t[0]
print 'List 1 trials recall rate during test: %s'%ser_corr_t[1]
if anal_s_dic['num_inc'] > 0:
    print 'probility to reacall each item during a trial in study(only with incorrect trials): %s'%pos_s
if anal_t_dic['num_inc'] > 0:
    print 'probility to reacall each item during a trial in test(only with incorrect trials): %s'%pos_t
