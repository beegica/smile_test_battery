# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:58:24 2015

@author: Paul Cheng
"""
#Global import
import os
import random
from random import shuffle


#################
##CONFIGURATION##
#################
#trial excution
do_practice_P_GO = True
do_P_GO = True
do_practice_R_GO = True
do_R_GO = True

#List Gene Config
#stimulus Present
responds = ['R','P']
isi_presenation = [u"☆",u"☆",u"☆",u"☆"]
TARGET_BLOCKS = ['P','P','R','R']
correct_key= 'SPACEBAR'
pract_P_target = TARGET_BLOCKS[0]
P_GO_target = TARGET_BLOCKS[1]
pract_R_target= TARGET_BLOCKS[2]
R_GO_target = TARGET_BLOCKS[3]
fn = 'arial-unicode-ms.ttf'


#Block_Config
NUM_BLOCK = 2
NUM_PRC_BLOCKS = 1
TARGET_RATIO = [0.80,0.20]
rep_num = 10 #number of times Target being represesnted
prac_rep_num = 5
GO = int(TARGET_RATIO[0]*10)
NOGO = int(TARGET_RATIO[1]*10)


#Timing
isi = 1.5
target_present_time = 0.5

#Instruction
inst_front = 30
inst_init = "In this experiment, you will be performing a task called the 'GO and No GO' task that tests your respond time to the item presented. You will see a series of 'P's and 'R's on the screen. Whenever you see a 'P' respond by pressing the space bar on the keyboard. DO NOT RESPOND when you see an 'R'. Most of the letters you see will be 'P's. You will have just over a second to make your response, so please do so as quickly as you can without sacrificing accuracy."
inst_p_go = "We are now about to start the actual experiment. The experiment will consist of one block that contains 160 trials. Again, in each trial Whenever you see a 'P' respond by pressing the space bar on the keyboard. DO NOT RESPOND when you see an 'R'. Whenever you are ready press any key to begin."
inst_r_go_prac = "You may take a short break before you continue.  In the second half of this study, the mapping will reverse.  This time, hit the space bar key only when you see the 'R', but not when you see a 'P'. Once again, most of the letters you see will be 'R's. You will begin with a few practice trials.  Press any key to begin."
inst_r_go = "Like the previous study block, this block will also contain 160 trails, and you will not longer get rated cue. So remember whenever you see a ‘R’ respond by pressing the space bar on the keyboard. DO NOT RESPOND when you see an ‘P’. Press any key to begin. "
inst_end = "Thank you for participating in our study, Press any key to exit the program."

###################
##LIST GENERATION##
###################
# DATA STRUCTURES
#
#
# blocks - list of dictionaries. Each element is a dictionary
#   with the following keys:
#       'Practice_P' - list of dictionaries, each containing data
#                          for a single Practice P GO trial. Keys are:
#               'block_num'         - block number as an integer (0 = practice block)
#               'trial_num'         - trial number within the block
#               'block_type'      - 'P_GO', 'R_GO'
#               'trial_type'     - 'GO', 'NOGO'
#               'trial_presenation'   - ['T',u"☆",u"☆",u"☆"], [u"☆",'T',u"☆",u"☆"],[u"☆",u"☆",'T',u"☆"],[u"☆",u"☆",u"☆",'T']
#               'target_pos'     - 'bottom_right', 'bottom_left, 'top_right','top_left'
#
#       'Practice_R' - same as above
#
#       'P_GO_block' - same as above
#
#       'R_GO_block' - sane as above
#
# EXPERIMENT DESIGN NOTES
#
# Trials per block = 40
#   within each block there are 4 repeations of 10 following stimulus
#   8  Target GO
#   2  Target NOGO
#
#Trials are randomized within blocks
#each Practice block contains one block and each target block has four blocks
#
#P GO blocks=  160 trials and R GO block = 160 trials
#adding up for 320 trials
#
#

def target_creater():
    """
    creating all the possible Target position

    """
    target_pos = [['T',u"☆",u"☆",u"☆"],
                  [u"☆",'T',u"☆",u"☆"],
                  [u"☆",u"☆",'T',u"☆"],
                  [u"☆",u"☆",u"☆",'T']]
    return target_pos

def trial_type(target,resp):
    """
    Loop around the target position and target stimulus to create a trial

    INPUT ARGS:
        target  - trial type target
        resp    - responds that could be generated on screen
    """


    GO_NOGO=['P','R']
    #deciding trial type: P-go or R-go
    #t = target, resp = responds
    for r in range(len(resp)):
        #asign trial GO and NO GO target
        if target == resp[r]:
            #Go
            GO_NOGO[0] = resp[r]


        else:
            #No GO
            GO_NOGO[1] = resp[r]


    return GO_NOGO

def block_rep(target, responds, rep_num, TARGET_RATIO):
    """
    Generating one block represenation( 40 trials)

    INPUT ARGS:
        target       - trial type target
        responds     - responds that could be generated on screen
        rep_num      - number of represenation in each trial
        TARGET_RATIO - ratio of Go and No Go trials
    """
    #setting up var to loop around to generate block rep
    GO_NOGO = trial_type(target,responds)
    br =[]
    GO = int(TARGET_RATIO[0]*rep_num)
    NOGO = int(TARGET_RATIO[1]*rep_num)
    GO_trials = GO*target_creater()
    NOGO_trials = NOGO*target_creater()
#    print GO
#    print NOGO
        #Loop over respond to asign target
    for g in range(len(responds)):
        #using if statement to asign P or R
        if responds[g] == GO_NOGO[0]:
            #loop over previous set GO trials and asigh target
            for t in range(len(GO_trials)):
                for present in range(len(GO_trials[t])):
                   if GO_trials[t][present] == 'T':
                       GO_trials[t][present]= responds[g]

                br.append(GO_trials[t])

        elif responds[g] == GO_NOGO[1]:
            for c in range(len(NOGO_trials)):
                for pt in range(len(NOGO_trials[c])):
                    if NOGO_trials[c][pt] == 'T':
                        NOGO_trials[c][pt]= responds[g]
                br.append(NOGO_trials[c])

    #shuffle the represenation
    random.shuffle(br)

    return br

def create_block(target, responds, rep_num, TARGET_RATIO, NUM_BLOCK, correct_key):

    block = []
    #loop over block
    for b in range(NUM_BLOCK):
        if NUM_BLOCK <= 1:
            print "creating practice %s_GO block %s" %(target,b+1)
        else:
            print "creating %s_GO block %s" %(target,b+1)
        rep= block_rep(target, responds, rep_num, TARGET_RATIO)
        responds = trial_type(target,responds)
        #loop over the trial definitions for the block
        for t in range(len(rep)):
            trial= dict()
            trial['block_type'] = '%s_GO' %(target)
            trial['trial_num']= t+1
            trial['block_num']= b+1
            trial['trial_presentation'] = rep[t]
            if NUM_BLOCK <= 1:
                trial['practice_block'] = True
            else:
                trial['practice_block'] = False


            #asign target position
            tl, tr, bl, br = rep[t]

            for r in responds:
                if tl == r:
                    trial['target_pos']= 'top_left'
                    if r == target:
                        trial['trial_type'] = 'GO'
                        trial['correct_respond']= correct_key
                    else:
                        trial['trial_type'] = 'NOGO'
                        trial['correct_respond']= None


                elif tr == r:
                    trial['target_pos']= 'top_right'
                    trial['correct_respond']= r
                    if r == target:
                        trial['trial_type'] = 'GO'
                        trial['correct_respond']= correct_key
                    else:
                        trial['trial_type'] = 'NOGO'
                        trial['correct_respond']= None

                elif bl == r:
                    trial['target_pos']= 'bottom_left'
                    trial['correct_respond']= r
                    if r == target:
                        trial['trial_type'] = 'GO'
                        trial['correct_respond']= correct_key
                    else:
                        trial['trial_type'] = 'NOGO'
                        trial['correct_respond']= None

                elif br == r:
                    trial['target_pos']= 'bottom_right'
                    trial['correct_respond']= r
                    if r == target:
                        trial['trial_type'] = 'GO'
                        trial['correct_respond']= correct_key
                    else:
                        trial['trial_type'] = 'NOGO'
                        trial['correct_respond']= None

            block.append(trial)

    return block
def experiement_block(pract_P_target, pract_R_target, P_GO_target, R_GO_target,
                  responds, prac_rep_num, rep_num, TARGET_RATIO, NUM_PRC_BLOCKS, NUM_BLOCK,
                  correct_key):
    # Create an empty list of trials
    blocks = {'practice_P_GO_trials':create_block(pract_P_target, responds, prac_rep_num, TARGET_RATIO, NUM_PRC_BLOCKS, correct_key),
             'practice_R_GO_trials':create_block(pract_R_target, responds, prac_rep_num, TARGET_RATIO, NUM_PRC_BLOCKS, correct_key),
             'P_GO_trials':create_block(P_GO_target, responds, rep_num, TARGET_RATIO, NUM_BLOCK, correct_key),
             'R_GO_trials':create_block(R_GO_target, responds, rep_num, TARGET_RATIO, NUM_BLOCK, correct_key)}
    return blocks
