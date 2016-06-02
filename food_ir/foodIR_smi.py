################################################################################
#
# foodIR_smi.py
#
# This experiment will display Savory and Sweet foods to the participant and
# ask them to make a keypress response. This experiment shows off how to use
#
#
#
################################################################################

# Import SMILE states
from smile.common import *
import os
import config
from list_gen import gen_blocks



# Set up an experiment instance
exp = Experiment()



inst_initial = open(config.inst_initial).read()
inst_test = open(config.inst_test).read()
deb =  open(config.debrief).read()



# Set up the blocks
# Call gen_blocks script
study_blocks,test_blocks = gen_blocks(config)



with If(config.do_study):
    # Loop over study blocks
    # Do instructions on first block of each session
    # Show initial inst
    # We've already completed this study block
    inst = Label(text = inst_initial,
                 font_size = config.text_size,
                 center_x=exp.screen.center_x,
                 center_y=exp.screen.center_y)
    with UntilDone():
        KeyPress()

    with Loop(study_blocks) as bl:
        # Press key to start block block
        Label(text= "Press any key for the next block.",
              font_size = config.text_size,
              text_size = (exp.screen.height,None),
              halign = 'center',
              valign = 'middle')
        with UntilDone():
            KeyPress()
        # Display a fixation cross
        Label(text = "+",
              font_size = config.fixation_size,
              duration = config.orient_duration)

        # Loop over the trials
        with Loop(bl.current) as t:

            with Parallel():
                # Present the trial based on timing from the config and trial
                Image(source = t.current['stim_path'],
                      log_on = True)
                Label(text = config.study_prompt,
                      center_y = (exp.screen.height/2- exp.screen.height/3),
                      font_size = config.text_size)
                study_stim_kp = KeyPress(keys = config.study_resp_keys)
            with UntilDone():
                Wait(duration = config.study_duration,
                     jitter= config.study_jitter_max)
            Log(t.current,
                keypress=study_stim_kp.pressed,
                response_time=study_stim_kp.rt)

    Label(text = "You are done with this portion of the experiment.",
          font_size = config.text_size)
    with UntilDone():
            KeyPress()


with If(config.do_test):
    # Do instructions on first block of each session
    # Show test inst
    Label(text = inst_test,
          font_size = config.text_size,
          halign= 'left',
          valign = 'middle')
    with UntilDone():
        KeyPress()


    with Loop(test_blocks) as tb:
        # Press key to start block block
        Label(text= "Press any key for the next block.",
              font_size = config.text_size,
              text_size = (exp.screen.height,None),
              halign = 'center',
              valign = 'middle')
        with UntilDone():
            KeyPress()


        # Display a fixation cross
        Label(text = "+",
              font_size = config.fixation_size,
              duration = config.orient_duration)

        # Loop over the trials
        with Loop(tb.current) as t:


            with Parallel():
                # Present the trial based on timing from the config and trial
                Image(source = t.current['stim_path'],
                             log_on = True)
                Label(text = config.test_prompt,
                                    center_y = (exp.screen.height/2 - 6*exp.screen.height/16),
                                    font_size = config.text_size)

                test_stim_kp = KeyPress(keys = config.test_resp_keys)
            with UntilDone():
                jitter = Wait(duration = config.test_duration,
                              jitter= config.test_jitter_max)


            Log(t.current,
                keypress= test_stim_kp.pressed,
                response_time=test_stim_kp.rt)

        Label(text = deb,
              font_size = config.text_size,
              halign= 'left',
              valign = 'middle')
    with UntilDone():
            kp= KeyPress()

exp.run()
