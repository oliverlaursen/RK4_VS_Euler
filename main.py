#unicode=utf-8

import numpy as np

n=50	 	# Antal iterationer
h=0.5	# Skridtlængde
startpunkt=(3,4)	#Startpunktet som løsningen skal gå igennem

def f(P0):
	"""
		Differentialligningen y' = f(x,y)
	"""
	P0x=P0[0]	# Tuplen slices for at får koordinaterne opdelt i to variable
	P0y=P0[1]
	return 0.5*x+y

def euler(diff, P0, n, h):
	"""
		Denne metode tilnærmer sig løsningen til differentialligningen diff,
		der går i gennem punktet P0. Tilnærmelsen afhænger af skridtlængden h
		og antal iterationer/gentagelser n
	"""
	P0x=P0[0]
	P0y=P0[1]
	xakse = np.linspace(P0x,n*h, n-(P0x/h)+1)	# List comprehension anvendes til at skabe en liste af x-aksens værdier
	print(xakse)


if __name__ == '__main__':
	euler(f,startpunkt, n,h)


