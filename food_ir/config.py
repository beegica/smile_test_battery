# Configuration for Food Item Recognition (foodIR) task
# to be run with DBS obesity subjects

# Select a mode to run in
mode = 'beh'

# For testing program, make it easy to select the phase
do_study = True
do_test = True

# The background color for the screen
# Gray20 cuts down on reflection
# Black is default
back_color = "gray20"

# Instruction files
inst_initial = 'text/inst_initial.txt'
inst_test = 'text/inst_test.txt'
debrief = 'text/debriefing.txt'
word_height_inst = .05
text_size = 25

# Stim pool
pool_dir = 'pools/food/images'
pool_file = 'pools/food/food.npy'

# List config
num_blocks = 4 # 32
list_len = 32 # 12
num_tries = 100
lag_range = [4,8] # [2,6]


stim_loc= (.5,.5)

# Pre-run fixation cross
fixation_height = .1
fixation_size = 65
orient_duration = 2.000

# Study config
study_min_duration = 0.200
study_prompt_size = .06
lock_study_to_TR = False

study_duration = 3.000
study_pre_delay = 0
study_jitter_max = 0.400
study_prompt = "Food or Non-Food"
study_resp_keys = ['J','K']
study_resp_mouse_buttons = [1,3]

# test config
test_min_duration = 0.200
test_prompt_size = .06

test_pre_delay = 0
test_duration = 3.000
min_resp_time = 0.200
test_jitter_max = 0.400
test_prompt = "Sure Old - Old - New - Sure New\n" + \
"       J            K       L               ;   "

test_resp_keys = ['J','K','L',';']
correct_target_resp = ['J','K']
correct_lure_resp = ['L',';']

# Realtime configuration
# ONLY MODIFY IF YOU KNOW WHAT YOU ARE DOING!
# HOWEVER, IT SHOULD BE TWEAKED FOR EACH MACHINE
doRealtime = True
rtPeriod = 0.120
rtComputation = 9.600
rtConstraint = 1.200









