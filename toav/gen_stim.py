import random

# List used to make the frequency of 1's at 25%
frequent = [1] * 30 + [0] * 10
random.shuffle(frequent)

# List used to make the frequency of 1's at 25%
rare = [0] * 30 + [1] * 10
random.shuffle(rare)
rare_dict = []
for i in rare:
    if i == 0:
        rare_dict.append({'offset':-20,
                        'response':None,
                        'condition': 'lure'})
    else:
        rare_dict.append({'offset':20,
                        'response':'Space',
                        'condition':'target'})

frequent_dict = []
for i in frequent:
    if i == 0:
        frequent_dict.append({'offset':-20,
                            'response':None,
                            'condition': 'lure'})
    else:
        frequent_dict.append({'offset':20,
                            'response':'Space',
                            'condition':'target'})