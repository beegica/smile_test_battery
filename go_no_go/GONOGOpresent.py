"""
Created on Tue Nov 17 16:38:12 2015

@author: Paul
"""

from smile.common import *
from smile.state import Subroutine

@Subroutine
def GONOGOpresent(self,Block_name, l =[], isi_p = [], fn= 'na', isi= 1, target_p_time= 2, center_x = 0, center_y = 0, screen_height= 0):
    # Loop over the Practice list and present it
    with Loop(l) as trial:
        # Prac_P trail sequence: pre-targetpresentations(1.5) --> Target conditions(0.5)
        with Serial():
            with Parallel():
                Label(text = isi_p[0],
                    color = 'WHITE',
                    center_x= center_x-screen_height/4,
                    center_y= center_y+screen_height/4,
                    font_size =(screen_height/2)-10,
                    font_name = fn)

                Label(text = isi_p[1],
                    color = 'WHITE',
                    center_x= center_x+ screen_height/4,
                    center_y= center_y+ screen_height/4,
                    font_size =(screen_height/2)-10,
                    font_name = fn)

                Label(text = isi_p[2],
                    color = 'WHITE',
                    center_x= center_x- screen_height/4,
                    center_y= center_y- screen_height/4,
                    font_size =(screen_height/2)-10,
                    font_name = fn)

                Label(text = isi_p[3],
                    color = 'WHITE',
                    center_x= center_x+ screen_height/4,
                    center_y= center_y- screen_height/4,
                    font_size =(screen_height/2)-10,
                    font_name = fn)
            # Run Parallel to pre-target presenations
            with UntilDone():
                Wait(isi)

            # Present target
            with Parallel():
                Label(text = trial.current['trial_presentation'][0],
                    color = 'WHITE',
                    center_x= center_x-screen_height/4,
                    center_y= center_y+screen_height/4,
                    font_size =(screen_height/2)-10,
                    font_name = fn)

                Label(text = trial.current['trial_presentation'][1],
                    color = 'WHITE',
                    center_x= center_x+ screen_height/4,
                    center_y= center_y+ screen_height/4,
                    font_size =(screen_height/2)-10,
                    font_name = fn)

                Label(text = trial.current['trial_presentation'][2],
                    color = 'WHITE',
                    center_x= center_x-screen_height/4,
                    center_y= center_y-screen_height/4,
                    font_size =(screen_height/2)-10,
                    font_name = fn)

                Label(text = trial.current['trial_presentation'][3],
                    color = 'WHITE',
                    center_x= center_x+ screen_height/4,
                    center_y= center_y- screen_height/4,
                    font_size =(screen_height/2)-10,
                    font_name = fn)

            with UntilDone():
                kp= KeyPress(keys=['SPACEBAR'],
                             duration= target_p_time,
                             correct_resp=trial.current['correct_respond'])


            # Practice session only feed back to participant's respond
            with If(trial.current['practice_block'] == True):
                with If((trial.current['trial_type'] == 'GO') & (kp.pressed == 'SPACEBAR')):
                        Rectangle(center_x= center_x,
                                center_y= center_y,
                                width= self._exp.screen.width,
                                height = screen_height/10,
                                color = 'WHITE',
                                duration = 0.8)
                        with Meanwhile():
                            lb1 = Label(text= 'Correct',color = 'GREEN',
                                center_x= center_x,
                                center_y= center_y,
                                font_size =35, duration= 0.8)


                with Elif((trial.current['trial_type'] == 'GO') & (kp.pressed == '')):
                    Rectangle(center_x= center_x,
                            center_y= center_y,
                            width= self._exp.screen.width,
                            height = screen_height/10,
                            color = 'WHITE',
                            duration = 0.8)
                    with Meanwhile():
                        lb2 = Label(text= 'Correct',color = 'RED',
                                center_x= center_x,
                                center_y= center_y,
                                font_size =35, duration= 0.8)


                with Elif((trial.current['trial_type'] == 'NOGO') & (kp.pressed == 'SPACEBAR')):
                    Rectangle(center_x= center_x,
                            center_y= center_y,
                            width= self._exp.screen.height,
                            height = screen_height/10,
                            color = 'WHITE',
                            duration = 0.8)
                    with Meanwhile():
                        lb3 = Label(text= 'ERROR',color = 'RED',
                                center_x= center_x,
                                center_y= center_y,
                                font_size =35, duration= 0.8)


                with Elif((trial.current['trial_type'] == 'NOGO') & (kp.pressed == '') ):
                    Rectangle(center_x= center_x,
                            center_y= center_y,
                            width= self._exp.screen.width,
                            height = screen_height/10,
                            color = 'WHITE',
                            duration = 0.8)
                    with Meanwhile():
                        lb4 = Label(text= 'Correct',color = 'GREEN',
                                center_x= center_x,
                                center_y= center_y,
                                font_size =35, duration= 0.8)

            # Log current trial
            Log(block_name = Block_name,
                trial_type = trial.current['trial_type'],
                block_type = trial.current['block_type'],
                block=trial.current['block_num'],
                trial=trial.current['trial_num'],
                stimulus_start_time= kp.start_time,
                stimulus_end_time = kp.end_time,
                response=kp.pressed,
                press_time=kp.press_time,
                rt=kp.rt,
                correct_respond = trial.current['correct_respond'],
                correct=kp.correct)
        # The grid that is being presented throughout the trial
        with Meanwhile():
            with Parallel():
                # Big REc
                Rectangle(center_x= center_x, center_y= center_y, width= screen_height, height = screen_height, color = 'WHITE')
                # Four small
                # Bottom_left
                Rectangle(center_x= center_x-screen_height/4, center_y= center_y- screen_height/4, width=(screen_height/2)-2, height = (screen_height/2)-2, color = 'BLACK')
                # Bottom_right
                Rectangle(center_x= center_x+ screen_height/4, center_y= center_y-screen_height/4, width=(screen_height/2)-2, height = (screen_height/2)-2, color = 'BLACK')
                # Top_left
                Rectangle(center_x= center_x- screen_height/4, center_y= center_y+ screen_height/4, width=(screen_height/2)-2, height = (screen_height/2)-2, color = 'BLACK')
                # Top_right
                Rectangle(center_x= center_x+ screen_height/4, center_y= center_y+ screen_height/4, width=(screen_height/2)-2, height = (screen_height/2)-2, color = 'BLACK')
