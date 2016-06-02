################################################################################
#
# gonogo_test.py
#
# This experiment tests people reaction time as well as their ability to inhibit
# their need to press the go button. Depending on the stimulus, they hit or
# don't hit a go button.
#
#
################################################################################


"""
    GO and NOGO EXPERIMENT STRUCTURES:
    1.  Instruction
    2.  Practice P GO
    3.  P GO experimential block
    4.  break and R GO instruction
    5.  R GO experimential block
"""


from smile.common import *
from GONOGOpresent import GONOGOpresent
from list_gen import *

# Generate the list
lis_blocks = experiement_block(pract_P_target, pract_R_target, P_GO_target, R_GO_target,
                  responds, prac_rep_num, rep_num, TARGET_RATIO, NUM_PRC_BLOCKS, NUM_BLOCK,
                  correct_key)

# Set up each part of experiments into list and list of dict
practice_P = lis_blocks['practice_P_GO_trials']
practice_R = lis_blocks['practice_R_GO_trials']
P_GO_block = lis_blocks['P_GO_trials']
R_GO_block = lis_blocks['R_GO_trials']


# Create an experiment
exp = Experiment()

Label(text = inst_init, text_size = (exp.screen.height,None),
      font_size = inst_front,
      halign= 'left',
      valign = 'middle')

with UntilDone():
    kp= KeyPress()

# If statement for testing
if do_practice_P_GO:

    prac_p_go = GONOGOpresent('Practice_P_GO', practice_P, isi_presenation, fn, isi, target_present_time, exp.screen.center_x,
                              exp.screen.center_y, exp.screen.height)


Label(text = inst_p_go,
      text_size = (exp.screen.height,None),
      font_size = inst_front,
      halign= 'left',
      valign = 'middle')
with UntilDone():
    kp= KeyPress()


# If statment for testing purposed
if do_P_GO:
    p_go = GONOGOpresent('P_GO',
                         P_GO_block,
                         isi_presenation,
                         fn,
                         isi,
                         target_present_time,
                         exp.screen.center_x,
                         exp.screen.center_y,
                         exp.screen.height)


Label(text = inst_r_go_prac,
      text_size = (exp.screen.height,None),
      font_size = inst_front,
      halign= 'left',
      valign = 'middle')
with UntilDone():
    kp= KeyPress()

if do_practice_R_GO:
    prac_r_go = GONOGOpresent('Practice_R_GO',
                              practice_R, isi_presenation,
                              fn,
                              isi,
                              target_present_time,
                              exp.screen.center_x,
                              exp.screen.center_y,
                              exp.screen.height)



Label(text = inst_r_go,
      text_size = (exp.screen.height,None),
      font_size = inst_front,
      halign= 'left',
      valign = 'middle')

with UntilDone():
    kp= KeyPress()


if do_R_GO:
    r_go = GONOGOpresent('R_GO',
                         R_GO_block,
                         isi_presenation,
                         fn,
                         isi,
                         target_present_time,
                         exp.screen.center_x,
                         exp.screen.center_y,
                         exp.screen.height)

# End of experiment
Label(text = inst_end,
      text_size = (exp.screen.height,None),
      font_size = inst_front,
      halign= 'left',
      valign = 'middle')
with UntilDone():
    kp= KeyPress()

exp.run()












##################
#Analizing Script#
##################


from smile.log import LogReader


# Acessing log
# LogReader will make slog file into a read able list of dic
P_log_stats=LogReader(filename = os.path.join(exp.subject_dir,'log_GONOGOpresent_179_1.slog'))
R_log_stats=LogReader(filename = os.path.join(exp.subject_dir,'log_GONOGOpresent_179_3.slog'))


# read_record() read a line in the slog dic. Also if this state is being loop over, it will
# List each dic in seq order
temp_P= P_log_stats.read_record()
temp_R= R_log_stats.read_record()


# An example of read record()
print 'this is P_GO: %s'%(temp_P)
print 'this is R_GO: %s'%(temp_R)


# Set the keys for later use
# Since both P and R has the same keys just use one set of keys
keys = temp_P.keys()


# Create a list of empty list to fit all the data in there
num_keys= len(keys)
list_keys = []
for k in range(num_keys):
    list_keys.append([])


# Use the zip function to asign Keys and all the data
stats_dict=dict(zip(keys, list_keys))


# print stats_dict
while temp_P != None:
    for name in keys:
        stats_dict[name].append(temp_P[name])
    temp_P=P_log_stats.read_record()


while temp_R != None:
    for name in keys:
        stats_dict[name].append(temp_R[name])
    temp_R =R_log_stats.read_record()


# Start generating analysis for veiwing.
go_trial_rt = []
error_omission = 0
error_commission = 0
total_go_trials = 0
total_nogo_trials = 0
miss = 0
correct = 0
total_trial_num = len(stats_dict['rt'])


for trial in range(len(stats_dict['trial_type'])):
    if stats_dict['trial_type'][trial] == 'GO':
        total_go_trials = total_go_trials+1

    else:
        total_nogo_trials = total_nogo_trials+1


# Calc rt and miss
for trial in range(len(stats_dict['trial_type'])):
    if (stats_dict['trial_type'][trial] == 'GO') & (stats_dict['correct'][trial] == True):
        # rt for go
        go_trial_rt.append(stats_dict['rt'][trial])
        correct = correct+1

    elif (stats_dict['trial_type'][trial] == 'GO') & (stats_dict['correct'][trial] == False):
        # Miss trails
        error_omission = error_omission+1
        miss= miss+1


# If the value is empty, correct will always set to false
# There for evoluate the NOGO task in following code


for trial in range(len(stats_dict['trial_type'])):
    if (stats_dict['trial_type'][trial] == 'NOGO') & (stats_dict['response'][trial] != 'SPACEBAR'):
        correct = correct+1

    elif (stats_dict['trial_type'][trial] == 'NOGO') & (stats_dict['response'][trial] == 'SPACEBAR'):
        # Error commission
        error_commission = error_commission+1
        miss = miss+1


average_go_rt = sum(go_trial_rt)/len(go_trial_rt)

print 'average responds time is %s seconds'%(average_go_rt)
print 'Miss: %s out of %s' %(miss, total_trial_num)
print 'Correct: %s out of %s'%(correct, total_trial_num)
print 'Error omission(aka GO error): %s out of %s'%(error_omission, total_go_trials)
print 'Error comission(aka NOGO error): %s out of %s'%(error_commission, total_nogo_trials)
