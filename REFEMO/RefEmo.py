#
#Refreshing Emotional stimuli
#   w/ refresh trials only (no repeat trials)
#

# global imports
import random
import config
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#local import 
from smile import *
from smile.audio import RecordSoundFile
from helper.list_gen import gen_blocks



########################
#prepare the experiment#
########################

# create an experiment
exp = Experiment()

# generate lists
blocks = gen_blocks(config)
#practice_block = 
refresh_blocks = [blocks[i]['refresh_trials'] for i in range(config.NUM_BLOCKS)]
rec_blocks = [blocks[i]['test_trials'] for i in range(config.NUM_BLOCKS)]
practice_ref_block = [blocks[i]['practice_trial'] for i in range(config.NUM_PRAC_BLOCKS)]
practice_rec_block = [blocks[i]['practice_test_trial'] for i in range(config.NUM_PRAC_BLOCKS)]
#print rec_blocks[0]

#read in the instruction
inst_initial = open(config.inst_initial).read()
inst_ref = open(config.inst_refresh).read()
inst_ref_p= open(config.inst_refresh_practice).read()
inst_ref_s= open(config.inst_refresh_start).read()
inst_t_p= open(config.inst_test_practice).read()
inst_t_s= open(config.inst_test_start).read()
deb= open(config.debrief).read()
bb = config.block_break

#testing lis_gene
#for b in practice_ref_block:
#   print b

#############
#Instruction#
#############

if config.do_instructions:
    #instruction for begining the experiment
    inst = Label(text = inst_initial,  
                 font_size= config.text_size,
                 text_size = (exp.screen.height,None), 
                 halign= 'center', 
                 valign = 'middle')                      
    with UntilDone():
        kp= KeyPress()

    
    #instruction for Refreshing
    inst_ref = Label(text= inst_ref, 
                    font_size= config.text_size,
                    text_size = (exp.screen.height,None), 
                    halign= 'center', 
                    valign = 'middle')   
    with UntilDone():
        kp= KeyPress()

###################
#Refreshing Trials#
###################
    
if config.do_study_task:                
    # loop over the trial
    #instruction for practice ref
    inst_ref_p = Label(text = inst_ref_p, 
                       font_size= config.text_size,
                       text_size = (exp.screen.height,None), 
                       halign= 'center', 
                       valign = 'middle')
    with UntilDone():
        kp= KeyPress()

    
    #Refresh Practice Experiement
    
    #start the cross for the practice experiment
    
    #Loop over the study blocks to indivdual block 
    with Loop(practice_ref_block) as block:        
        
        # ask for key press before each block
        txt = Label(text = bb, 
                    font_size = config.text_size)                   
        with UntilDone():
            KeyPress()        
        
        #Loop over the blocks to trial
        with Loop(block.current) as trial:
            cross_1= Label(text = config.fixation_text, 
                         font_size= config.fixation_size,
                         duration = config.study_fixation_duration)
            #show the stimulus
            with Parallel():
                #show down stimuli
                d_stim = Label(text= trial.current['down_stim']['name'],
                               center_y= (exp.screen.height/2- 65), 
                               font_size= config.stim_txt_size,
                               duration = config.stim_duration) 
                #show up stimuli
                u_stim = Label(text = trial.current['up_stim']['name'], 
                               center_y= (exp.screen.height/2+ 65), 
                               font_size= config.stim_txt_size,
                               duration = config.stim_duration)
               
        #load the refresh item and show an arrow
            with If(trial.current['refresh_side']== 'UP'):
                
                #refresh up-side
                arrow = Label(text= config.up_arrow, 
                             font_size = config.arrow_size,
                             font_name = config.fn)
                #Recording 
                with UntilDone():
                    rec = RecordSoundFile(filename= trial.current['audio_name'], 
                                    duration = config.arrow_duration)
                    
                    
                              
                #refresh down-side
            with Else():
                
                #refresh up-side
                arrow = Label(text= config.down_arrow, 
                             font_size = config.arrow_size,
                             font_name = config.fn)
                #Recording 
                with UntilDone():
                    rec = RecordSoundFile(filename= trial.current['audio_name'], 
                                    duration = config.arrow_duration)
                    
                    
            #ISI           
            cross_2= Label(text = config.fixation_text, 
                         font_size= config.fixation_size,
                         duration = config.pause_after_ref_trial)
                
            #log the practice experiment
            Log(trial.current,
                refresh_start = rec.rec_start,
                refresh_end = rec.end_time,
                cross_1_start_time = cross_1.start_time,
                cross_1_end_time = cross_1.end_time)
                
                
                
                


    
    #instruction to start the experiment
    inst_ref_s = Label(text = inst_ref_s, 
                       font_size= config.text_size,
                       text_size = (exp.screen.height,None), 
                       halign= 'center', 
                       valign = 'middle')
    with UntilDone():
        kp= KeyPress()

    
    #Refresh Experiement
    #Loop over the study blocks to indivdual block    
    with Loop(refresh_blocks) as block:
       
        # ask for key press before each block
        txt = Label(text = bb, 
                    font_size = config.text_size)                   
        with UntilDone():
            KeyPress()
                    
        #Loop over the blocks to trial
        with Loop(block.current) as trial:
            cross_1= Label(text = config.fixation_text, 
                         font_size= config.fixation_size,
                         duration = config.study_fixation_duration)
        
            #show the stimulus
            with Parallel():
                
                #show down stimuli
                d_stim = Label(text= trial.current['down_stim']['name'],
                               center_y= (exp.screen.height/2- 65), 
                               font_size= config.stim_txt_size,
                               duration = config.stim_duration)
                
                #show up stimuli
                u_stim = Label(text = trial.current['up_stim']['name'], 
                               center_y= (exp.screen.height/2+ 65), 
                               font_size= config.stim_txt_size,
                               duration = config.stim_duration)
               
        #load the refresh item and show an arrow
            with If(trial.current['refresh_side']== 'UP'):
                
                #refresh up-side
                arrow= Label(text= config.up_arrow, 
                             font_size = config.arrow_size,
                             font_name = config.fn)
                #Recording 
                with UntilDone():
                    rec = RecordSoundFile(filename= trial.current['audio_name'], 
                                          duration = config.arrow_duration)
                    
                    
                  
                        
                #refresh down-side
            with Else():
                
                #refresh up-side
                arrow= Label(text= config.down_arrow, 
                             font_size = config.arrow_size,
                             font_name = config.fn)
                #Recording 
                with UntilDone():
                    rec = RecordSoundFile(filename= trial.current['audio_name'], 
                                          duration = config.arrow_duration)
                    
                    
                    
                    
            #ISI                    
            cross_2= Label(text = config.fixation_text, 
                         font_size= config.fixation_size,
                         duration = config.pause_after_ref_trial)
                
            #log the practice experiment
            Log(trial.current,
                refresh_start = rec.rec_start,
                refresh_end = rec.end_time,
                cross_1_start_time = cross_1.start_time,
                cross_1_end_time = cross_1.end_time)
    
####################  
# Recogition Trials#
####################   

# loop over regnition trials in the block
if config.do_recog_test:
    
    #instruction for Suprise Recongition trials
    inst_t_p = Label(text = inst_t_p, 
                     font_size= config.text_size,
                     text_size = (exp.screen.height,None), 
                     halign= 'center', 
                     valign = 'middle')
    with UntilDone():
        KeyPress()
    
    #start the practice test block
    with Loop(practice_rec_block) as block:
    
        # ask for key press before each block
        txt = Label(text = bb, 
                    font_size = config.text_size)
                    
        with UntilDone():
            KeyPress()
                
        #loop over blocks to create trials 
        with Loop(block.current) as trial:
                
            # present the test stimulus and ask for key respond
            stim = Label(text = trial.current['test_stim']['name'],
                         font_size = config.stim_txt_size,
                         halign= 'center', 
                         valign = 'middle')
            
            # Present the key presss question
            #for reason of eyeball effect not to ask this questions 
            #it will be stated exlicitly in the instruciton
            #txt = label(text = 'Old (J) or New (K) ?',
#                         text_size = (exp.screen.height,None))

            #acepting key responds 
            with UntilDone():            
                key = KeyPress(keys = config.test_resp_keys, 
                               correct_resp = trial.current['correct_resp'], 
#                               base_time=stim['last_flip']['time'], 
                               duration= config.test_max_resp_time)           
            # Log what is happening
            Log(trial.current,
#                txt_on = stim['last_flip'],
                resp = key.pressed,
                rt = key.rt,
                correct = key.correct)
                                             
            # pause in between Stimuulus       
            Wait(config.pause_after_test_trial)   

    
    #start the test blocks
    inst = Label(text = inst_t_s,
                 font_size= config.text_size,
                 text_size = (exp.screen.height,None), 
                 halign= 'center', 
                 valign = 'middle')
    with UntilDone():
        kp= KeyPress()
            
    #loop over the recogntion blocks
    with Loop(rec_blocks) as block:
    
        # ask for key press before each block
        txt = Label(text = bb, 
                    font_size = config.text_size)                   
        with UntilDone():
            KeyPress()
                
        #loop over blocks to create trials 
        with Loop(block.current) as trial:
                
            # present the test stimulus and ask for key respond
            stim = Label(text = trial.current['test_stim']['name'],
                         font_size= config.stim_txt_size,
                         text_size = (exp.screen.height,None), 
                         halign= 'center', 
                         valign = 'middle')
            
            # Present the key presss question
            #for reason of eyeball effect not to ask this questions 
            #it will be stated exlicitly in the instruciton
            #txt = label(text = 'Old (J) or New (K) ?',
#                         text_size = (exp.screen.height,None))
                           
            #acepting key responds 
            with UntilDone():            
                key = KeyPress(keys = config.test_resp_keys, 
                               correct_resp = trial.current['correct_resp'], 
#                               base_time=stim['last_flip']['time'], 
                               duration= config.test_max_resp_time)           
      
            # pause in between Stimuulus       
            ISI = Wait(config.pause_after_test_trial)
            
            # Log what is happening
            Log(trial.current,
                stimulus_on = stim.start_time,
                respose = key.pressed,
                press_time = key.press_time,
                rt = key.rt,
                correct = key.correct)
                                             
                                      
 
    

############
#Debriefing#
############
debrief = Label(text = deb, 
                font_size = config.debrief_text_size, 
                text_size = (exp.screen.height,None), 
                halign= 'center', 
                valign = 'middle')
                
with UntilDone():
    KeyPress()

exp.run()
#exp.run(trace=True)
 
