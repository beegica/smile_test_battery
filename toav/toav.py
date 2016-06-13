################################################################################
#
# toav.py
#
# Test of Attentional Vigilance. In this task, a white square appears briefly on
# the screen, with a black square within it. Participant must respond only to
# targets--the black square on top. For the first half of the test, targets are
# rare; for the second half, they are frequent.
#
#
################################################################################


from smile.common import *
from config import *
from gen_stim import *

# Setup Subroutine for displaying the
# Rectangles
@Subroutine
def Target(self,
            offset = 20,
            correct_resp = 'Space',
            JITTER = 0.5,
            fixDur = 1,
            onStimDur = 0.75,
            width=100):
    target = Rectangle(color = 'white', width = width*.75, height = width*.75)
    with Meanwhile():
        Rectangle(bottom = Ref.cond(offset > 0, target.bottom + offset, target.top + offset - width*.1), color = 'black', width = width*.10, height = width*.10)
    with UntilDone():
        Wait(.2)
        kp = KeyPress(keys = ['SPACEBAR'], duration = onStimDur, correct_resp = correct_resp, base_time = target.appear_time['time'])
        Wait(0.5)
        self.correct_resp = kp.correct_resp
        self.rt = kp.rt


# Start Experiment
exp = Experiment(background_color = 'black')



Label(text = instruct)
with UntilDone():
    KeyPress()


with Loop(rare_dict) as trial:
    Label(text = '+', duration = FIX_DUR, font_size=FONT_SIZE)
    Rtarget = Target(onStimDur=ON_STIM_DUR,JITTER=STIM_JITTER,
                     offset = trial.current['offset'],
                     correct_resp = trial.current['response'],
                     width=exp.screen.height*.3)
    Wait(ISI,JITTER)
    Log(name='Rare', correct=Rtarget.correct_resp, reaction_time=Rtarget.rt, condition = trial.current['condition'])



with Loop(frequent_dict) as trial:
    Label(text = '+', duration = FIX_DUR,font_size=FONT_SIZE)
    Rtarget = Target(onStimDur=ON_STIM_DUR,JITTER=STIM_JITTER,
                     offset = trial.current['offset'],
                     correct_resp = trial.current['response'],
                     width=exp.screen.height*.3)
    Wait(ISI,JITTER)
    Log(name='Frequent', correct=Rtarget.correct_resp, reaction_time=Rtarget.rt, condition = trial.current['condition'])
Label(text = 'End of Experiment', duration = 1)

exp.run()
#End of experiment
