################################################################################
#
# match_to_sample.py
#
# Show a matrix of squares at the center of the screen. The participant needs to
# pick, out of 2 newly displayed matricies, which matrix is a repeat of the one
# shown before.
#
#
################################################################################


from smile.common import *
import random

#Global Variables
NUM_OF_TRIALS = 40
SIZE_OF_BOX = 20

@Subroutine
def ProduceTarget(self,
                    coordinate_offsets = [],
                    color_list = [],
                    x_offset = 0,
                    correct_resp = None,
                    onStimDur = 0.75):
        with Parallel():
            target = Rectangle(color = color_list[0], right = exp.screen.center_x - x_offset - SIZE_OF_BOX,
            center_y = exp.screen.center_y, width = SIZE_OF_BOX, height = SIZE_OF_BOX)
            Rectangle(color = color_list[1], right= exp.screen.center_x - x_offset,
            center_y = exp.screen.center_y, width = SIZE_OF_BOX, height = SIZE_OF_BOX)
            Rectangle(color = color_list[2], left = exp.screen.center_x + x_offset,
            center_y = exp.screen.center_y, width = SIZE_OF_BOX, height = SIZE_OF_BOX)
            Rectangle(color = color_list[3], left = exp.screen.center_x + SIZE_OF_BOX + x_offset,
            center_y = exp.screen.center_y, width = SIZE_OF_BOX, height = SIZE_OF_BOX)
            Rectangle(color = color_list[4], right = exp.screen.center_x - x_offset - SIZE_OF_BOX,
            center_y = exp.screen.center_y + SIZE_OF_BOX, width = SIZE_OF_BOX, height = SIZE_OF_BOX)
            Rectangle(color = color_list[5], right = exp.screen.center_x - x_offset,
            center_y = exp.screen.center_y + SIZE_OF_BOX, width = SIZE_OF_BOX, height = SIZE_OF_BOX)
            Rectangle(color = color_list[6], left = exp.screen.center_x + x_offset,
            center_y = exp.screen.center_y + SIZE_OF_BOX, width = SIZE_OF_BOX, height = SIZE_OF_BOX)
            Rectangle(color = color_list[7], left = exp.screen.center_x + SIZE_OF_BOX + x_offset,
            center_y = exp.screen.center_y + SIZE_OF_BOX, width = SIZE_OF_BOX, height = SIZE_OF_BOX)
            Rectangle(color = color_list[8], right = exp.screen.center_x - SIZE_OF_BOX - x_offset,
            center_y = exp.screen.center_y + 2 * SIZE_OF_BOX, width = SIZE_OF_BOX, height = SIZE_OF_BOX)
            Rectangle(color = color_list[9], right = exp.screen.center_x - x_offset,
            center_y = exp.screen.center_y + 2 * SIZE_OF_BOX, width = SIZE_OF_BOX, height = SIZE_OF_BOX)
            Rectangle(color = color_list[10], left = exp.screen.center_x + x_offset,
            center_y = exp.screen.center_y + 2 * SIZE_OF_BOX, width = SIZE_OF_BOX, height = SIZE_OF_BOX)
            Rectangle(color = color_list[11], left = exp.screen.center_x + SIZE_OF_BOX + x_offset,
            center_y = exp.screen.center_y + 2 * SIZE_OF_BOX, width = SIZE_OF_BOX, height = SIZE_OF_BOX)
            Rectangle(color = color_list[12], right = exp.screen.center_x - x_offset - SIZE_OF_BOX,
            center_y = exp.screen.center_y + 3 * SIZE_OF_BOX, width = SIZE_OF_BOX, height = SIZE_OF_BOX)
            Rectangle(color = color_list[13], right = exp.screen.center_x - x_offset,
            center_y = exp.screen.center_y + 3 * SIZE_OF_BOX, width = SIZE_OF_BOX, height = SIZE_OF_BOX)
            Rectangle(color = color_list[14], left = exp.screen.center_x + x_offset,
            center_y = exp.screen.center_y + 3 * SIZE_OF_BOX, width = SIZE_OF_BOX, height = SIZE_OF_BOX)
            Rectangle(color = color_list[15], left = exp.screen.center_x + SIZE_OF_BOX + x_offset,
            center_y = exp.screen.center_y + 3 * SIZE_OF_BOX, width = SIZE_OF_BOX, height = SIZE_OF_BOX)





trial_dict = []
for x in range(NUM_OF_TRIALS):
    color_list1 = []
    color_list2 = []
    for x in range(17):
        if (x % 2 == 0):
            color_list1.append("red")
            color_list2.append("red")
        else:
            color_list1.append("yellow")
            color_list2.append("yellow")
    random.shuffle(color_list1)
    random.shuffle(color_list2)

    left_right_list = []
    for x in range(NUM_OF_TRIALS):
        if(x % 2 == 0):
            left_right_list.append(["F", -100, "J", 100])
        else:
            left_right_list.append(["J", 100, "F", -100])
    random.shuffle(left_right_list)

    trial_dict.append({"target":color_list1,
                        "lure": color_list2,
                        "correct":left_right_list[x][0],
                        "correct-x-offset":left_right_list[x][1],
                        "incorrect":left_right_list[x][2],
                        "incorrect-x-offset":left_right_list[x][3]})



exp = Experiment(background_color = 'black')



Label(text = """This experiment is called match to sample task. You will see a
colored matrix and study it for a period of time. Then you are shown a pair of
matrices; one identical, and one different. You will then choose which one is the
one you studied. Press F if the matrix on the left is identical to the one studied,
Press J if the matrix on the right is identical to the one studied. Press any key
when you are ready to begin. """)
with UntilDone():
    KeyPress()

Label(text = "Start of Experiment", duration = 2)
with Loop(trial_dict) as trial:
    ProduceTarget(color_list = trial.current["target"])
    with UntilDone():
        Wait(2)
    Wait(2)
    with Parallel():
        correct = ProduceTarget(color_list = trial.current["target"],
            x_offset = trial.current["correct-x-offset"], correct_resp = trial.current["correct"])

        incorrect = ProduceTarget(color_list = trial.current["lure"],
            x_offset = trial.current["incorrect-x-offset"])
    with UntilDone():
        Wait(.2)
        kp = KeyPress(keys = ["F", "J"], correct_resp = trial.current["correct"], duration = 1.8)

    Log(name = "trial", correct = kp.correct_resp, reaction_time = kp.rt, condition = trial.current["correct"])

exp.run()
