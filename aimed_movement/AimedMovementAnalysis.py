from smile.log import LogReader
import numpy as np
from matplotlib import pyplot as plt
import os.path

subNum = 1
rects = {}
N = 0
#reads in subject slog files. 'directory' needs to be edited with directory used to store slog files
while(os.path.exists('directory' + str(subNum) + '/log_AimMove_0.slog')):
	l = LogReader(filename = 'directory' + str(subNum) + '/log_AimMove_0.slog')
	temp = l.read_record()
	while(temp != None):
		rect = {}
		rect['size'] = temp['targsize']
		rect['totDist'] = temp['targdist']
		rect['totRt'] = temp['rt']
		rect['count'] = 1
		if rect['size'] not in rects:
			rects[rect['size']] = rect
			N += 1
		else:
			rects[rect['size']]['totDist'] += rect['totDist']
			rects[rect['size']]['count'] += 1
			rects[rect['size']]['totRt'] += rect['totRt']	
		temp = l.read_record()	
	subNum += 1
i = 0
ind = np.arange(N)
avgSpeed = []

for size in rects:
	avgSpeed.append((rects[size]['totDist']/ rects[size]['count'])/(rects[size]['totRt']/ rects[size]['count']))
plt.bar(ind, avgSpeed, 0.5, color='b')
plt.xticks(ind + 0.25, rects.keys())
plt.yticks(np.arange(0, 1200, 50))
plt.title("Average Reaction Speed for Different Size Rectangles")
plt.ylabel("Average Reaction Speed(Pixels/Second)")
plt.xlabel("Size of Rectangle(Pixels)")

plt.show()
