# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:08:37 2015

@author: Paul
"""
from smile.log import LogReader

###########################
#Setting up for processing#
###########################
#acessing log

P_log_stats=LogReader(filename = 'data/1004/log_GONOGOpresent_179_1.slog')
R_log_stats=LogReader(filename = 'data/1004/log_GONOGOpresent_179_3.slog')

#read_record() read a line in the slog dic. Also if this state is being loop over, it will
#list each dic in seq order
temp_P= P_log_stats.read_record()
temp_R= R_log_stats.read_record()

#an example of read record()
print 'this is P_GO: %s'%(temp_P)
print 'this is R_GO: %s'%(temp_R)

#print all the keys of log
#print temp_P.keys()
#print temp_R.keys()

#set the keys for later use
#since both P and R has the same keys just use one set of keys
keys = temp_P.keys()

#create a list of empty list to fit all the data in there
num_keys= len(keys)
list_keys = []
for k in range(num_keys):
    list_keys.append([])

#Use the zip function to asign Keys and all the data     
stats_dict=dict(zip(keys, list_keys))
#print stats_dict
while temp_P != None:
    for name in keys:    
        stats_dict[name].append(temp_P[name])
    temp_P=P_log_stats.read_record()

while temp_R != None:
    for name in keys:    
        stats_dict[name].append(temp_R[name])
    temp_R =R_log_stats.read_record()

##Start generating analysis for veiwing.
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

#calc rt and miss
for trial in range(len(stats_dict['trial_type'])):
    if (stats_dict['trial_type'][trial] == 'GO') & (stats_dict['correct'][trial] == True):
        #rt for go
        go_trial_rt.append(stats_dict['rt'][trial])
        correct = correct+1
    
    elif (stats_dict['trial_type'][trial] == 'GO') & (stats_dict['correct'][trial] == False):
        #miss trails
        error_omission = error_omission+1
        miss= miss+1
#        print stats_dict['trial_type'][trial]
        
#If the value is empty, correct will always set to false
#There for evoluate the NOGO task in following code

for trial in range(len(stats_dict['trial_type'])):
    if (stats_dict['trial_type'][trial] == 'NOGO') & (stats_dict['response'][trial] != 'SPACEBAR'):     
        correct = correct+1 
    
    elif (stats_dict['trial_type'][trial] == 'NOGO') & (stats_dict['response'][trial] == 'SPACEBAR'):
        #Error commission
#        print stats_dict['trial_type'][trial]
#        print stats_dict['correct'][trial]
        error_commission = error_commission+1
        miss = miss+1

average_go_rt = sum(go_trial_rt)/len(go_trial_rt)
#average_miss = error_omission/total_go_trials
        
print 'average responds time is %s seconds'%(average_go_rt)
print 'Miss: %s out of %s' %(miss, total_trial_num)
print 'Correct: %s out of %s'%(correct, total_trial_num)
print 'Error omission(aka GO error): %s out of %s'%(error_omission, total_go_trials)
print 'Error comission(aka NOGO error): %s out of %s'%(error_commission, total_nogo_trials)    