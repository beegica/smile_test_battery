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
            onStimDur = 0.75):
    target = Rectangle(color = 'white', width = 75, height = 75)
    with Meanwhile():
        Rectangle(center_y = self.exp.screen.center_y + offset, color = 'black', width = 10, height = 10)
    with UntilDone():
        Wait(.2)
        kp = KeyPress(keys = ['SPACE'], duration = onStimDur, correct_resp = correct_resp, base_time = target.appear_time['time'])
        Wait(0.5)
        self.correct_resp = kp.correct_resp
        self.rt = kp.rt


# Start Experiment
exp = Experiment(background_color = 'black')

Label(text = instruct)
with UntilDone():
    KeyPress()
Label(text = 'Start of Experiment', duration = 3,font_size=FONT_SIZE)
with Loop(rare_dict) as trial:
    Label(text = '+', duration = FIX_DUR, font_size=FONT_SIZE)
    Rtarget = Target(offset = trial.current['offset'], correct_resp = trial.current['response'])
    Wait(ISI,JITTER)
    Log(name='Rare', correct=Rtarget.correct_resp, reaction_time=Rtarget.rt, condition = trial.current['condition'])

with Loop(frequent_dict) as trial:
    Label(text = '+', duration = FIX_DUR,font_size=FONT_SIZE)
    Rtarget = Target(onStimDur=ON_STIM_DUR,JITTER=STIM_JITTER,offset = trial.current['offset'], correct_resp = trial.current['response'])
    Wait(ISI,JITTER)
    Log(name='Frequent', correct=Rtarget.correct_resp, reaction_time=Rtarget.rt, condition = trial.current['condition'])
Label(text = 'End of Experiment', duration = 1)

exp.run()
#End of experiment
