#unicode=utf-8

import numpy as np

n=50	 	# Antal iterationer
h=0.1	# Skridtlængde
startpunkt=(0,1)	#Startpunktet som løsningen skal gå igennem

def f(P0):
	"""
		Differentialligningen y' = f(x,y)
	"""
	P0x=P0[0]	# Tuplen slices for at får koordinaterne opdelt i to variable
	P0y=P0[1]
	return 0.5*P0x+P0y

def euler(diff, P0, n, h):
	"""
		Denne metode tilnærmer sig løsningen til differentialligningen diff,
		der går i gennem punktet P0. Tilnærmelsen afhænger af skridtlængden h
		og antal iterationer/gentagelser n
	"""
	P0x=P0[0]
	P0y=P0[1]
	xakse = np.arange(P0x,n*h+P0x, h)		# X-aksen skabes med h stort mellemrum imellem hver værdi.
	yakse=[P0y,]
	
	for i in range(n-1):
		yvalue=round(yakse[i]+h*diff((xakse[i], yakse[i])), 5)
		yakse.append(yvalue)

	return yakse

def rk4(diff, P0, n, h):
	P0x=P0[0]
	P0y=P0[1]
	xakse=np.arrange(P0x, n*h+P0x+h, h)



if __name__ == '__main__':
	euler(f,startpunkt, n,h)


