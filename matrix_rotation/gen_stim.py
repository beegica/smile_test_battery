from config import *
import random
import numpy as np
from sys import argv
#generate study matrices based on number of desired trials
for i in range(numOfTrials):
	matrix = []
	row = []
	tops = []
	lefts = []
	digitMatrix = []
	digitRow = []
	# set the color of squares in matrix
	for j in range(1, size*size+1):
		rand = random.randint(0, 500)
		color = "GRAY"
		colorNum = 0
		if(rand > 250):
			color = "RED"
			colorNum = 1
		row.append(color)
		digitRow.append(colorNum)
		tops.append(top)
		lefts.append(left)
		if(j % 6 == 0):
			left = 0
			top -= 100
			matrix.append(row)
			digitMatrix.append(digitRow)
			digitRow = []
			row = []
		else:
			left += 100
	top = 0
	#add matrix, the numerical representaiton of the matrix, height and width of the squares, the locations of the squares and the trial number
	matrices.append({'Matrix': matrix, 'DigMatrix': digitMatrix, 'height': 95, 'width':95, 'tops': tops,
			'lefts': lefts, 'Trial': trial})
	trial+=1

#generate test matrices and add it, its numerical representation, the direction of rotation and target response to the dictionary
for matrix in matrices:
    rotRand = random.randint(0, 900)
    #rotated right
    if(rotRand <= 300):
        matrix['RotationMatrix'] = np.rot90(matrix['Matrix'], 3)
        matrix['DigitRotMat'] = ''.join(str(element) for row in np.rot90(matrix['DigMatrix'],3) for element in row)
        matrix['Rotation'] = "Right"
        matrix['Target'] = 'J'


    #rotated left matrix
    elif(rotRand > 300 and rotRand <= 600):
	    matrix['RotationMatrix'] = np.rot90(matrix['Matrix'])
	    matrix['DigitRotMat'] = ''.join(str(element) for row in np.rot90(matrix['DigMatrix']) for element in row)
	    matrix['Rotation'] = "Left"
   	    matrix['Target'] = 'J'
    #generate new matrix
    else:
	lureMatrix = []
	row = []
	digitMatrix = []
	digitRow = []
	for j in range(1, size*size+1):
		rand = random.randint(0,500)
		color = "GRAY"
		colorNum = 0
		if(rand > 250):
			color = "RED"
			colorNum = 1
		digitRow.append(colorNum)
		row.append(color)
		if(j % 6 == 0):
			lureMatrix.append(row)
			digitMatrix.append(digitRow)
			digitRow = []
			row = []
	matrix['RotationMatrix'] = lureMatrix
	matrix['Rotation'] = "No Rotation"
	matrix['DigitRotMat'] = ''.join(str(element) for row in digitMatrix for element in row)
    matrix['Target'] = 'K'
    #transforms the study and test matrices into one dimensional arrays
    oneDimArrayMat = []
    for i in matrix['Matrix']:
        print i
    	oneDimArrayMat += [i]
    matrix['Matrix'] = oneDimArrayMat
    oneDimArrayMat = []

    for i in matrix['RotationMatrix']:
    	oneDimArrayMat += [i]
    matrix['RotationMatrix'] = oneDimArrayMat
    matrix['DigMatrix'] = ''.join(str(element) for row in matrix['DigMatrix'] for element in row)