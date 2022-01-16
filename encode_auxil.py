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
		else:
			m.append(int(bin(i)[2:]))
	return m


def split(word):
   	return [char for char in word]

