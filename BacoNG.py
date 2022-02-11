from art import *
from PIL import Image
import numpy
import encode_auxil as binary
import math
import os

menu_options = {
	1: 'Prepare Your Image',
	2: 'Encode Message',
	3: 'Decode Message',
	4: 'Exit',
}

brand = text2art("BacoNG", font="small")

def print_mod():
	os.system('cls||clear')
	print(brand)

def print_menu():
	for key in menu_options.keys():
		print (key, '--', menu_options[key] )

def option1():
	global image
	image = input('Please enter the image path:')
	prep_im = Image.open(image)
	array = numpy.array(prep_im)
	print('Height: ', array.shape[0])
	print('Width: ', array.shape[1])
	message_length = math.floor(array.shape[1]/7)
	print('Total Message Length: ', message_length)
	
	# Loop 'zero-ing' out the picture
	for h in range(array.shape[0]):
		for w in range(array.shape[1]):
			array[h,w,3] = 255
	
	new_im = Image.fromarray(array)
	new_im.save(image)	

def option2():
	global height
	global width
	global depth
	global image

	image = input('Please enter the image path: ')
	im = Image.open(image)
	num_array = numpy.array(im)
	width = num_array.shape[1]
	userInput = input('Please enter the text to encode: ')
	message = encode(str(userInput), num_array)
	#print(message)
	new_im = Image.fromarray(message)
	fileName = input('Name of output file: ')
	new_im.save(fileName)
	print(fileName, " written!")

def option3():
	global image
	image = input('Please enter the image path: ')
	print('Attempting to decode: ', image)
	print('\n', decode(image), '\n')


# === Encode Message to Array Function === #

def encode(string, num_array):
		testArray = binary.toBinary(string)
		arrayPosition = 0
		array = [1]*(width)
		new_array = []
		new_array = [0 for i in range(len(string))]

		for j in range(len(string)):
			#print(j)
			letter = binary.split(str(testArray[j]))
			print(letter)
			loopControl = len(letter)
			k = 0
			while k < loopControl:
				if letter[k] == '0':
					array[arrayPosition] = array[arrayPosition] - 1
				else:
					array[arrayPosition] = array[arrayPosition]
				arrayPosition = arrayPosition + 1
				k = k + 1
			#array[arrayPosition] = array[arrayPosition] - 2 
		message = array
		for i in range(width):
			#new_array[i] = num_array[0,i].item(3) - message[i]
			num_array[0,i,3] = num_array[0,i,3] - message[i]
		return(num_array)


def decode(image):
	de_im = Image.open(image)
	array = numpy.array(de_im)
	output = []
	sep = ''
	k = 0
	j = 0

# Loop through pixels to construct binary

	while j < len(array):
		for l in range(7):
			if array[0,k,3] == 254:
				output.append('1')
			else:
				output.append('0')
			k = k + 1
			j = j + 1
		output.append(',')
		j = j + 1

	stringBinary = sep.join(output)
	#print(stringBinary)
	characterBinary = stringBinary.split(',')
	j = 0
	finalMessage = []

	for j in range(len(characterBinary)-1):
		characterASCII = int(characterBinary[j], base=2)
		q = chr(characterASCII)
		finalMessage.append(q)
		fM = sep.join(finalMessage)
	return(fM)

if __name__=='__main__':
	print_mod()
	while(True):
		print_menu()
		option = ''
		try:
			option = int(input('Enter your choice: '))
		except:
			print('Wrong input. Please enter a number...')
		if option == 1:
			option1()
		elif option == 2:
			option2()
		elif option == 3:
			option3()
		elif option == 4:
			print('Cya!')
			exit()
		else:
			print('Invalid option. Please enter a number between 1 and 4.')
