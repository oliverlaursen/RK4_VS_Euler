#unicode=utf-8

import numpy as np
import matplotlib.pyplot as plt

n=50	 	# Antal iterationer
h=0.1	# Skridtlængde
startpunkt=(0,1)	#Startpunktet som løsningen skal gå igennem

def f(P0):
	"""
		Differentialligningen y' = f(x,y)
	"""
	P0x=P0[0]	# Tuplen slices for at får koordinaterne opdelt i to variable
	P0y=P0[1]
	return 0.5*P0x*P0y

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
		yvalue=yakse[i]+(h*diff(xakse[i], yakse[i]))
		yakse.append(yvalue)

	return yakse

def rk4(diff, P0, n, h):
	P0x=P0[0]
	P0y=P0[1]
	xakse=np.arange(P0x, n*h+P0x, h)
	yakse=[P0y,]

	for i in range(n-1):
		k1=h*diff(xakse[i],yakse[i])
		k2=h*diff(xakse[i]+(h/2), yakse[i]+(k1/2))
		k3=h*diff(xakse[i]+(h/2), yakse[i]+(k2/2))
		k4=h*diff(xakse[i]+h, yakse[i]+k3)

		yvalue=yakse[i]+((1/6)*(k1+(2*k2)+(2*k3)+k4))
		yakse.append(yvalue)

	return yakse

def draw_graph(data,names,h,P0x,functions=None):
	"""
		Denne funktion optegner grafer ud fra y-værdierne data, skridtlængde h og startværdi P0x
		Optegning af funktioner vil være muligt ved angivelse af functions parameteren

		data er en liste af y-værdier som skal optegnes

		Hver løsning opgivet i data skal have samme skridtlængde h og samme startpunkt P0x, dog
		kan n variere.

	"""
	plt.xlabel('x')
	plt.ylabel('y')


	for i in range(len(data)):
		n=len(data[i])		# n kan findes for hver løsning ud fra længden af listen for dataet
		xaxis=np.arange(P0x, n*h+P0x, h)
		plt.plot(xaxis,data[i],marker='o',label=names[i])

	if functions is not None:
		largestn=0
		for i in data:
			if len(i)>largestn:
				largestn=len(i)		# Finder den største n for at bestemme x-aksen til funktionerne
		largestxaxis=np.arange(P0x, largestn*h+P0x,h)

		for i in range(len(functions)):
			plt.plot(largestxaxis,functions[i](largestxaxis),label=names[i+len(data)])

	plt.legend(loc='upper left')
	plt.show()







