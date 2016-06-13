from config import *
import random
import numpy as np

xPos = 0
yPos = 0


#generate study matrices based on number of desired trials
for i in range(numOfTrials):
    matrix = []
    row = []
    yPositions = []
    xPositions = []
    digitMatrix = []
    digitRow = []
    # set the color and numerical representation of each square in matrix, gray for 0 and red for 1
    for j in range(1, size*size+1):
        rand = random.randint(0, 500)
        color = "GRAY"
        colorNum = 0
        if(rand > 250):
            color = "RED"
            colorNum = 1
        row.append(color)
        digitRow.append(colorNum)
        yPositions.append(yPos)
        xPositions.append(xPos)
        if(j % size == 0):
            xPos = 0
            yPos -= 100
            matrix.append(row)
            digitMatrix.append(digitRow)
            digitRow = []
            row = []
        else:
            xPos += 100
    yPos = 0
    #add matrix, the numerical representaiton of the matrix, height and width of the squares, the locations of the squares and the trial number
    matrices.append({'Matrix': matrix, 'DigMatrix': digitMatrix, 'height': 95, 'width':95, 'yPositions': yPositions,
                     'xPositions': xPositions, 'Trial': trial})
    trial+=1

#generate test matrices and add it, its numerical representation, the direction of rotation and target response to the dictionary
for matrix in matrices:
    rotRand = random.randint(0, 900)
    #rotated right
    if(rotRand <= 300):
        matrix['RotationMatrix'] = np.rot90(matrix['Matrix'], 3)
        #transform the digit representation of the right rotated matrix into a string
        matrix['DigitRotMat'] = ''.join(str(element) for row in np.rot90(matrix['DigMatrix'],3) for element in row)
        matrix['Rotation'] = "Right"
        matrix['Target'] = 'J'


    #rotated left matrix
    elif(rotRand > 300 and rotRand <= 600):
        matrix['RotationMatrix'] = np.rot90(matrix['Matrix'])
        #transform the digit representation of the left rotated matrix into a string
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
            if(j % size == 0):
                lureMatrix.append(row)
                digitMatrix.append(digitRow)
                digitRow = []
                row = []
        matrix['RotationMatrix'] = lureMatrix
        matrix['Rotation'] = "No Rotation"
        #transofrm the digit representation of the lure matrix into a string
        matrix['DigitRotMat'] = ''.join(str(element) for currentRow in digitMatrix for element in currentRow)
        matrix['Target'] = 'K'
    #convert the digit representation of the study matrix into a string
    matrix['DigMatrix'] = ''.join(str(element) for currentRow in matrix['DigMatrix'] for element in currentRow)

    #transforms the study and test matrices into one dimensional arrays
    oneDimArrayMat = []
    for i in matrix['Matrix']:
    	oneDimArrayMat += i
    matrix['Matrix'] = oneDimArrayMat

    oneDimArrayMat = []
    for i in matrix['RotationMatrix']:
    	oneDimArrayMat += i
    matrix['RotationMatrix'] = oneDimArrayMat
