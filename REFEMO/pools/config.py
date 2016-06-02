# -*- coding: utf-8 -*-
#
# Configuration for RefEmo stimulus norming
#

# Tasks to do (change as necesasry for testing)
do_instructions = True
do_study_task = True
do_recog_test = True

# Master display parameters
#
# Background color for the screen (default = black)
# gray20 cuts down on reflection
back_color = "gray20"

###########
# STIMULI##
###########

# Pool files
poolFile = 'pools/RefEmo_stimuli_rev.csv'
# log path
log_path = 'data/'
# Ranges for selection preselected pools
# valence
val_range = {'pos':(6.85,8.34),
             'neg':(1.80,3.63),
             'neu':(4.52,6.35)}
# arousal
aro_range = {'pos':(3.46,7.35),
             'neg':(3.63,7.35),
             'neu':(2.50,7.35)}


###############################
# EXPERIMENT DESIGN PARAMETERS#
###############################

# Divide the task into blocks to allow subjects periodic rests
NUM_BLOCKS = 7
NUM_PRAC_BLOCKS = 1


# Define the minumum composition of a refresh block
#   4  +~  (+~ refresh L, +~ refresh R, ~+ refresh L, ~+ refresh R)
#   4  +~  (-~ refresh L, -~ refresh R, ~- refresh L, ~- refresh R)
#   2  ~~  (refresh U, refresh D)
#              valences   Up     Down    refresh
prac_block_def= [('pos-neg','pos','neg','up'),
                 ('pos-neg','pos','neg','down'),
                 ('pos-neg','neg','pos','up'),
                 ('pos-neg','neg','pos','down')]

block_def = [('pos-neg','pos','neg','up'),
             ('pos-neg','pos','neg','down'),
             ('pos-neg','neg','pos','up'),
             ('pos-neg','neg','pos','down'),
             ('pos-neu','pos','neu','up'),
             ('pos-neu','pos','neu','down'),
             ('pos-neu','neu','pos','up'),
             ('pos-neu','neu','pos','down'),
             ('neg-neu','neg','neu','up'),
             ('neg-neu','neg','neu','down'),
             ('neg-neu','neu','neg','up'),
             ('neg-neu','neu','neg','down'),
             ('neu-neu','neu','neu','up'),
             ('neu-neu','neu','neu','down')]
# How many of these can we put in a single study block
block_reps = 2
practice_block_reps = 1

####################
# EXPERIMENT TASKS##
####################

# Instructions
# Font size for instructions (proportion of vertical screen)
word_height_inst = .05
text_width = 1200
text_size = 25
debrief_text_size = 15
# instruction text files
inst_initial = 'inst/inst_init.txt'
inst_refresh = 'inst/inst_refresh.txt'
inst_refresh_practice = 'inst/inst_refresh_prac.txt'
inst_refresh_start = 'inst/inst_refresh_start.txt'
inst_test_practice = 'inst/inst_test_prac.txt'
inst_test_start = 'inst/inst_test_start.txt'
debrief = 'inst/debriefing.txt'
block_break= 'Press any key for the next block.'

# Refreshing task
#
# Fixation
study_fixation_duration = 0.5
study_fixation_jitter = 0.5
fixation_text = ' + '
fixation_height = .15 # proportion of vertical screen
fixation_size = 46
# Stimulus presentation
stim_duration = 1.65
stim_jitter = 0.5
wordHeight = .1
stim_txt_size = 46
#arrow pointer
arrow_size = 46
up_arrow = u'⇧'
down_arrow = u"\u21E9"
arrow_duration = 2.000
fn = 'arial-unicode-ms.ttf'
# after refresh trial
pause_after_ref_trial = 1.5
jitter_after_ref_trial = 0.5

# Recognition test
# fixation
pretest_fixation_duration = 0
pretest_fixation_jitter = None
pretest_pause = 0
pretest_jitter = None
# test stimulus presentation
#test_image_yscale = .3
#test_image_xscale = test_image_yscale*4/3.
#image_offset = (.0,.0)
# response keys and prompt
test_resp_keys = ['J','K']
test_keymap = {'J':'OLD','K':'NEW'}
test_prompt = 'OLD  or  NEW\n' + ' J            K '
# max time for response
test_max_resp_time = 1.5
# Intertrial interval
pause_after_test_trial = 1.5
jitter_after_test_trial = 0
