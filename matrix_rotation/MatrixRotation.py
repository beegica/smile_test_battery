from smile.common import *
from smile.log import LogReader

from gen_stim import *
import config
exp = Experiment()

Label(text="A series of two matrices will appear on the screen during each trial \
      . A study matrix, which will appear for 2 seconds, and a test matrix. \
      The test matrix will either be the study matrix rotated left or right, or a completly new matrix. When prompted press J if the test matrix is the same matrix as the study matrix, just rotated, or K if it is a new matrix. Press any key to continue", font_size=20,text_size=(exp.screen.width/1.5, None),
      haline= 'center',valine= 'middle')
with UntilDone():
	KeyPress()

#displays study matrix for 2 seconds followed by test matrix and waits until response is pressed then logs necessary information
with Loop(matrices) as matrix:
	with Parallel():
	    for column in range(size*size):
	        Rectangle(left = exp.screen.left + exp.screen.width/3.5 + matrix.current['lefts'][column],
	                  top = exp.screen.top - 20 + matrix.current['tops'][column],
			  width = matrix.current['width'],
			  height = matrix.current['height'],
			  color = matrix.current['Matrix'][column])
	with UntilDone():
		Wait(2)

 	with Parallel():
	    for column in range(size*size):
	        Rectangle(left = exp.screen.left + exp.screen.width/3.5 + matrix.current['lefts'][column],
	                  top = exp.screen.top - 20 + matrix.current['tops'][column],
			  width = matrix.current['width'],
			  height = matrix.current['height'],
			  color = matrix.current['RotationMatrix'][column])
	    Label(text="Press J if the matrix is the same", font_size=30,
		bottom = exp.screen.bottom, left = exp.screen.left+ exp.screen.width/8)
	    Label(text="Press K if the matrix is the different", font_size=30,
		bottom = exp.screen.bottom, right = exp.screen.right - exp.screen.width/7)

	with UntilDone():
		kp = KeyPress(keys = key_dic, correct_resp = matrix.current['Target'])
		Wait(0.5)

	l=Log(name='MatRot',
            trial=matrix.current['Trial'],
	    matrix= matrix.current['DigMatrix'],
	    rotMatrix= matrix.current['DigitRotMat'],
	    rotation= matrix.current['Rotation'],
            resp=kp.correct,
            respTime=kp.rt)

exp.run()








