################################################################################
#
# AimedMovement.py
#
# Tests subjects reaction time by asking them to move the mouse cursor from a
# starting point to sequentially presented rectangles. The rectangles will have
# a shuffled size and distance from the starting point.
#
#
################################################################################

# Import SMILE states
from smile.common import *
from random import shuffle
from sys import argv

# Experiment Variables
positions = [100,125,150,250,400,550,750]
subject = argv[0]
widths = [10,20,40]
i = 0
numOfTrials = 50
rects = []

# Generate list of rectangles and their positions
for i in range(numOfTrials):
    shuffle(widths)
    shuffle(positions)
    rects.append({'left' : positions[0], 'width' : widths[0], 'trial' : i+1})

# Start defining the experiment
exp = Experiment()

# Show the Instructions
Label(text='Move the mouse from the white starting rectangle to the red rectangle that appears as quickly as possible. To begin each trial move the mouse back to the starting rectangle. Press any key to begin', font_size=20,text_size=(exp.screen.width/1.5, None) ,haline= 'center', valine= 'middle')
with UntilDone():
    KeyPress()

# Causes the rectangles to appear and wait for the
# mouse cursor to reach the red rectangle
with Loop(rects) as pos:
    start = Rectangle(left = 50, width = 25, height = 25, color = 'white')
    with UntilDone():
       Wait(until=MouseWithin(start))
       Wait(.2)

    rect = Rectangle(left = pos.current['left'], width = pos.current['width'],
                     height = 50, color = 'red')
    with UntilDone():
       w = Wait(until=MouseWithin(rect))

    # Log all the info for this trial
    Log(name= 'AimMove',
        subject=subject,
        trial=pos.current['trial'],
        targdist=rect.x - start.x,
        targsize=rect.width*rect.height,
        rt=w.event_time['time'] - rect.appear_time['time'])

# After defining the experiment above, run the experiment
exp.run()
