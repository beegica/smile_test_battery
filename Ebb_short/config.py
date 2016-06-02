"""
Created on Mon Dec 14 12:56:13 2015

@author: Paul
"""

do_instructions= True
do_study_phase = True
do_test_phase = True
do_cvc_words= True

cvcspool= 'pools/cvcs.txt'
wordspool= 'pools/words.txt'

num_word_list = 8
num_block = 2
conditions = ['nonsense_cvc', 'normal_cvc']
text_size = 45
inst_front = 35
keys = ['1','2','3','4','5','6','7','8']
number_loop = ['3','2','1']
isi = 2
stim_on_time = 0.5
count_down_timing= 0.5 # per presented item total of four items
num_corr_need = 2




meaningless_intro = "In this task, you will see a list of %s meaningless syllables.\
Afterwards, you will be shown a screen with all of the syllables and be asked to choose the original order.\
Choose all syllables, and when you are complete hit the 'done' bottom with your mouse, the comptuer will determine whether you were correct.\
Each list will repeat until you correctly remember the entire list twice in a row.\
Once you do this, you will move to the next list. \
You will learn a total of %s lists."%(num_word_list, num_block)

cvc_intro = "In this task, you will see a list of %s 3 Letter words. \
Afterwards, you will be shown a screen with all of the syllables and be asked to choose the original order.\
Choose all syllables, and when you are complete hit the 'done' bottom with your mouse, the comptuer will determine whether you were correct.\
Each list will repeat until you correctly remember the entire list twice in a row. \
Once you do this, you will move to the next list.\
You will learn a total of %s lists."%(num_word_list, num_block)


testing_phase_instruction = " Now, you will be shown the same 2 lists you have just learned. Try to learn them again."

deb= "Thank you for participating."

number_instr = " Please enter numbers from 1 to 8!"
