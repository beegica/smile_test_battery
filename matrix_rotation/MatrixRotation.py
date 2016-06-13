from smile.common import *
from smile.video import Screenshot
import random
import numpy as np
from gen_stim import *
from config import *

exp = Experiment()


# Present the instructions
Label(text=instruct, font_size=20,text_size=(exp.screen.width/1.5, None),
      haline= 'center', valine= 'middle')
with UntilDone():
    KeyPress()

# Displays study matrix for 2 seconds followed by test matrix and waits until response is pressed then logs necessary information
with Loop(matrices) as matrix:
    # Parallel setting up original matrix
    with Parallel() as pp1:
        with Loop(range(size*size)) as lp1:
            with pp1.insert():
                Rectangle(left = exp.screen.width/2-(matrix.current['width']*size/2) + matrix.current['xPositions'][lp1.i],
                          top = exp.screen.top - 20 + matrix.current['yPositions'][lp1.i],
                          width = matrix.current['width'],
                          height = matrix.current['height'],
                          color = matrix.current['RotationMatrix'][lp1.i])
    with UntilDone():
        Wait(2)

    # Parallel setting up the rotated matrix
    with Parallel() as pp2:
        with Loop(range(size*size)) as lp2:
            with pp2.insert():
                Rectangle(left = exp.screen.width/2-(matrix.current['width']*size/2) + matrix.current['xPositions'][lp2.i],
                          top = exp.screen.top - 20 + matrix.current['yPositions'][lp2.i],
                          width = matrix.current['width'],
                          height = matrix.current['height'],
                          color = matrix.current['Matrix'][lp2.i])
        lb = Label(text="Press J if the matrix is the same", font_size=30,
                bottom = exp.screen.bottom, left = exp.screen.left+ exp.screen.width/8)
        Label(text="Press K if the matrix is the different", font_size=30,
                bottom = exp.screen.bottom, right = exp.screen.right - exp.screen.width/7)

    with UntilDone():
        Wait(until=lb.appear_time)
        kp = KeyPress(keys=key_dic, correct_resp = matrix.current['Target'], base_time=lb.appear_time['time'])
        Wait(0.5)

	Log(name='MatRot',
          trial=matrix.current['Trial'],
	      matrix= matrix.current['DigMatrix'],
	      rotMatrix= matrix.current['DigitRotMat'],
	      rotation= matrix.current['Rotation'],
          resp=kp.correct,
          respTime=kp.rt)

exp.run()








