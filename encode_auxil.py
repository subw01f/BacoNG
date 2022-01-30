import math
import binascii
from art import *


def toBinary(a):
	l,m=[],[]
	for i in a:
		l.append(ord(i))
	for i in l:
		print(i)
		if i == 32:
			m.append(str("0100000"))
		elif i == 33:
			m.append(str("0100001"))
		elif i == 34:
			m.append(str("0100010"))
		elif i == 35:
			m.append(str("0100011"))
		elif i == 36:
			m.append(str("0100100"))
		elif i == 37:
			m.append(str("0100101"))
		elif i == 38:
			m.append(str("0100110"))
		elif i == 39:
			m.append(str("0100111"))
		elif i == 40:
			m.append(str("0101000"))
		elif i == 41:
			m.append(str("0101001"))
		elif i == 42:
			m.append(str("0101010"))
		elif i == 43:
			m.append(str("0101011"))
		elif i == 44:
			m.append(str("0101100"))
		elif i == 45:
			m.append(str("0101101"))
		elif i == 46:
			m.append(str("0101110"))
		elif i == 47:
			m.append(str("0101111"))
		elif i == 48:
			m.append(str("0110000"))
		elif i == 49:
			m.append(str("0110001"))
		elif i == 50:
			m.append(str("0110010"))
		elif i == 51:
			m.append(str("0110011"))
		elif i == 52:
			m.append(str("0110100"))
		elif i == 53:
			m.append(str("0110101"))
		elif i == 54:
			m.append(str("0110110"))
		elif i == 55:
			m.append(str("0110111"))
		elif i == 56:
			m.append(str("0111010"))
		elif i == 57:
			m.append(str("0111001"))
		elif i == 58:
			m.append(str("0111010"))
		elif i == 59:
			m.append(str("0111011"))
		elif i == 60:
			m.append(str("0111100"))
		elif i == 61:
			m.append(str("0111101"))
		elif i == 62:
			m.append(str("0111110"))
		elif i == 63:
			m.append(str("0111111"))
		else:
			m.append(int(bin(i)[2:]))
	return m


def split(word):
   	return [char for char in word]



