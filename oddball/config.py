# config

NUM_REPS = 2
NUM_RARE = 1
NUM_COMMON = 5
STIMS = {'visual':['X','O'],
         'auditory':['BEEP','BOOP']}
FREQS = {'BEEP':800, 
         'BOOP':400}

RESPS = ['J','K']
MODES = STIMS.keys()
CONDS = ['common']*NUM_COMMON + ['rare']*NUM_RARE


# timing
AUDIO_DUR = .5
AUDIO_ISI = 1.5
VISUAL_DUR = 1.0
VISUAL_ISI = 1.0
JITTER = .5
MIN_RT = .100
RESP_DUR = 1.25

# inst info
INST_FILE = 'text/inst_odd.rst'
INST2_FILE = 'text/inst_final.rst'
INST_BASE_FONT_SIZE = 42

# pulse info
DO_PULSES = False
PAUSE_BETWEEN_PULSES = 3.0
JITTER_BETWEEN_PULSES = 3.0

# text size
FONT_SIZE = 42

DEBRIEF_FILE = 'text/debriefing.txt'



