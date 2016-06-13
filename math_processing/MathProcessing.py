################################################################################
#
# MathProcessing.py
#
# This experiment shows the participant mathmatical statement and then asks them
# to identify whether the statement evaluates to greater than or less than 5.
#
#
################################################################################


from smile.common import *
from smile.log import LogReader
from random import shuffle
from sys import argv
subject = argv[0]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
operators = ["+", "-"]
numOfTrials = 50
equations = []
key_dic = ['J', 'K']
FONT_SIZE = 50
maxDuration = 4
ISI = 0.5


# Generates list of dictionaries containing an equation, the correct answer and the trial number
for i in range(numOfTrials):
    sumOfNum = 0
    shuffle(numbers)
    shuffle(operators)
    op1 = operators[0]
    if(op1 == "+"):
        sumOfNum = numbers[0] + numbers[1]
    else:
        sumOfNum = numbers[0] - numbers[1]
    shuffle(operators)
    op2 = operators[0]
    if(op2 == "+"):
        sumOfNum = sumOfNum + numbers[2]
    else:
        sumOfNum = sumOfNum - numbers[2]
    answer = 'J'
    if(sumOfNum < 5):
        answer = 'K'

    equations.append({'Equation' : str(numbers[0]) + op1 + str(numbers[1])
                      + op2 + str(numbers[2]),
                      'Answer' : answer, 'trial' : i+1})



# Experiment start!
exp = Experiment()


Label(text="A series of equations will appear one at a time on the screen. " +
      "Press j if the equation is greater than 5 or k if it is less than 5 "+
      "Press any key to begin",font_size=30,
      text_size=(exp.screen.width/1.5, None), haline='center',valine='middle')
with UntilDone():
   	 KeyPress()


# Presents the equation and logs the keypress made by the subject as well as the trial number, equation presented, the correct answer, the response, and the response rate
with Loop(equations) as eq:
    Label(text="+", duration=ISI,font_size=FONT_SIZE)
    Wait(ISI)
    with Parallel():
     	Label(text="Press j if greater than 5", font_size=FONT_SIZE, bottom = exp.screen.bottom, left = exp.screen.left+ exp.screen.width/8)
     	Label(text="Press k if less than 5", font_size=FONT_SIZE, bottom = exp.screen.bottom, right = exp.screen.right - exp.screen.width/7)
     	Label(text=eq.current['Equation'], font_size=FONT_SIZE)
    with UntilDone():
         kp = KeyPress(keys = key_dic, duration = maxDuration, correct_resp = eq.current['Answer'])

    Log(name='MathProc',
        subject=subject,
        trial=eq.current['trial'],
        equation=eq.current['Equation'],
        answer=eq.current['Answer'],
        resp=kp.correct,
        respTime=kp.rt)



exp.run()





