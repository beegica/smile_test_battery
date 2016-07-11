from smile.common import *
from smile.pulse import JitteredPulses
from smile.audio import Beep, init_audio_server

import copy
import random
import numpy as np
import config
import os

exp = Experiment()
init_audio_server()


###### LIST GENERATION ######
#############################

# Each response mapped to each stimulus
blocks = []
for mode in config.MODES:
    for reverse_stim in [True, False]:
        # pick the proper stim set
        stims = config.STIMS[mode]
        # reverse if required
        if reverse_stim:
            stims = stims[::-1]
        # map to common and rare
        stim = {'common':stims[0],
                'rare':stims[1]}

        # loop over response mappings
        for reverse_resp in [True, False]:
            # pick the responses
            resps = config.RESPS[:]
            if reverse_resp:
                resps = resps[::-1]
            # make the mapping
            resp = {'common':resps[0],
                    'rare':resps[1]}

            # shuffle the conds
            random.shuffle(config.CONDS)

            # make the block
            block = [{'cond':cond,
                      'modality':mode,
                      'common_stim':stim['common'],
                      'rare_stim':stim['rare'],
                      'common_resp':resp['common'],
                      'rare_resp':resp['rare'],
                      'stim':stim[cond],
                      'correct_resp':resp[cond]}
                     for cond in config.CONDS]

            # append to blocks
            blocks.append(block)

# shuffle the blocks
random.shuffle(blocks)

# update with block and trial number
b=t=0
for block in blocks:
    for trial in block:
        trial.update({'block_num':b,'trial_num':t})
        t+=1
    b+=1

###### START/INSTRUCTIONS ######
################################

# first set up pulsing
if config.DO_PULSES:
    with Meanwhile():
        JitteredPulses(pause_between=config.PAUSE_BETWEEN_PULSES,
                       jitter_between=config.JITTER_BETWEEN_PULSES)

# Initialize visual states
Wait(2)
Label(text=' ',duration=.5)


# show instructions
RstDocument(text=open(config.INST_FILE, 'r').read(),
            base_font_size=config.INST_BASE_FONT_SIZE,
            width=800, height=exp.screen.height, )
with UntilDone():
    KeyPress(keys=['ENTER'])

# stimuli examples
Label(text="Press any key to see the visual stimuli.", font_size=config.FONT_SIZE)
with UntilDone():
    KeyPress()
# show visual stimuli
with Loop(config.STIMS['visual']) as stim:
    Label(text=stim.current, font_size=config.FONT_SIZE, duration=config.VISUAL_DUR)
    Wait(0.5)
Label(text="Press any key to hear the auditory stimuli.", font_size=config.FONT_SIZE)
with UntilDone():
    KeyPress()
# play auditory stimuli
with Loop(config.STIMS['auditory']) as stim:
    with Parallel():
        Beep(freq=Ref.getitem(config.FREQS,stim.current), duration=1.0, volume=1.0)
        with Meanwhile():
            Label(text=stim.current, font_size=config.FONT_SIZE)
    Wait(0.5)

# final instructions (set response mappings)
RstDocument(text=open(config.INST2_FILE, 'r').read(),
            base_font_size=config.INST_BASE_FONT_SIZE,
            width=800, height=exp.screen.height, )

with UntilDone():
    KeyPress(keys=['ENTER'])

###### DEFINE SUBROUTINES ######
################################

@Subroutine
# Key mappings for block
def InstReminder(self, fstim, sstim, mstim, duration=None):
    Wait(.5)
    with Parallel():

        # display modality of the block
        Label(text=mstim+' block response mapping:',
              center_x=exp.screen.center_x,
              center_y=exp.screen.center_y+(config.FONT_SIZE*2.5),
              font_size=config.FONT_SIZE)

        # Present key mapping
        r = Label(text='For '+fstim+', press '+config.RESPS[0] +
                  '\nFor '+sstim+', press '+config.RESPS[1],
                  font_size=config.FONT_SIZE*1.5)
        with If(duration == None):
            with Serial():
                # Request SPACE keypress
                Label(text='Press <SPACE> to continue.',
                      font_size=config.FONT_SIZE,
                      center_y=r.center_y-(config.FONT_SIZE*2.5))
                with UntilDone():
                        KeyPress(keys=['SPACEBAR'])
        # If duration is set, proceed without keypress
    with UntilDone():
        with If(duration == None): # can't use is
            KeyPress(keys=['SPACEBAR'])
        with Else():
            Wait(duration)


@Subroutine
# visual trial
def VisTrial(self, stim, corr, config):
    Wait(config.VISUAL_ISI)
    with Parallel():
        # Present the stimulus
        stimV = Label(text=stim, font_size=config.FONT_SIZE, duration=config.VISUAL_DUR)
        with Serial():
            Wait(config.MIN_RT)
            # Accept a keypress
            kpV = KeyPress(keys = config.RESPS,
                 duration = config.RESP_DUR,
                 base_time = stimV.appear_time['time'],
                 correct_resp=corr)
    # Set variables to log
    self.pressed = kpV.pressed
    self.press_time = kpV.press_time
    self.rt = kpV.rt
    self.stim_on_time = stimV.appear_time['time']
    self.correct = kpV.correct



@Subroutine
# auditory trial
def AudTrial(self, stim, corr, config):
    Wait(config.AUDIO_ISI)
    with Parallel():
    # Play the beep
        stimA = Beep(duration=config.AUDIO_DUR,
                     volume = 1.0,
                     freq=Ref.getitem(config.FREQS,trial.current['stim']))
        with Serial():
            Wait(config.MIN_RT)
            # Accept a keypress
            kpA = KeyPress(keys = config.RESPS,
                 duration = config.RESP_DUR,
                 base_time = stimA.sound_start_time,
                 correct_resp=corr)
    # Set variables to log
    self.pressed = kpA.pressed
    self.press_time = kpA.press_time
    self.rt = kpA.rt
    self.stim_on_time = stimA.sound_start_time
    self.correct = kpA.correct

###### EXPERIMENT ######
########################

with Loop(blocks) as block:

    # Choose inputs for block instructions
    exp.mstim=block.current[0]['modality']
    with If(block.current[0]['rare_resp']==config.RESPS[0]):
        exp.fstim=block.current[0]['rare_stim']
        exp.sstim=block.current[0]['common_stim']
    with Else():
        exp.fstim=block.current[0]['common_stim']
        exp.sstim=block.current[0]['rare_stim']

    with Serial():
        # Give instruction reminder
        InstReminder(exp.fstim, exp.sstim, exp.mstim)

        # Present the stimulus
        with Loop(block.current) as trial:

            # If visual trial, present label
            with If(trial.current['modality']=='visual'):
                exp.tr = VisTrial(trial.current['stim'],trial.current['correct_resp'],config)
            # If auditory trial, play beep
            with Else():
                    Label(text='+', font_size=config.FONT_SIZE)
                    with UntilDone():
                        exp.tr = AudTrial(trial.current['stim'],trial.current['correct_resp'],config)
            Log(trial.current,
                name='oddball',
                pressed=exp.tr.pressed,
                press=exp.tr.press_time,
                rt=exp.tr.rt,
                stim_on_time = exp.tr.stim_on_time,
                correct = exp.tr.correct,
                info=exp.info)

# Add in a little wait
Wait(1.0)

# Thank you at end
if False:
    RstDocument(source=config.DEBRIEF_FILE,
                base_font_size=config.INST_BASE_FONT_SIZE,
                size=(800, exp.screen.height))
    with UntilDone():
        KeyPress(keys=['ENTER'])
else:
    # Present done
    Label(text='Done!', font_size=config.FONT_SIZE, duration=2.0)
if __name__ == '__main__':
    exp.run()












