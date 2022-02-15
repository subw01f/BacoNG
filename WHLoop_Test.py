from art import *
from PIL import Image
import numpy
import encode_auxil as binary
import math
import os


# Plan is to import image into numpy array 

global image


 # array[h,w,rgbo(3 for opactiy)]

image = input('Please enter the image path:')
prep_im = Image.open(image)
array = numpy.array(prep_im)
print('Height: ', array.shape[0])
print('Width: ', array.shape[1])
pixelCount = array.shape[0]*array.shape[1]

newArray = [1] * pixelCount

print(newArray)
i = 0
j = 0
# Grab image width and load into variable

# Iterate loop with length of width array

testArray = binary.toBinary("teststringteststringteststringteststringteststringteststringteststringteststringteststringteststring")



letter = binary.split(str(testArray[j]))

print(letter)

print(letter[0])

#print(testArray)

for h in range(array.shape[0]):
		for w in range(array.shape[1]):
			i = i + 1
			j = j + 1

			#print(array[h,w,3])
