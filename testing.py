#unicode=utf8

from main import *
from math import *


def beregn_præcision(a,b):
	"""
		Beregner den gennemsnitlige overensstemmelse i procent af listen a i forhold til listen b
		Listerne må KUN indeholde floats
	"""
	kvadratsumfejl=0
	shortestlist=None

	if len(a)>len(b):
		shortestlist=b 		# Den korteste liste findes, for at undgå fejl med list index i loop ved gennemløb af liste
	else:
		shortestlist=a

	for i in range(len(shortestlist)):
		kvadratsumfejl+=(a[i]-b[i])**2

	return kvadratsumfejl

def get_eksakt_values(f,n,h, P0x):
	"""
		Beregner funktionsværdierne for en funktion f som starter ved x=P0x med n antal iterationer og h stor skridtlængde
	"""
	values=[]
	for i in range(n):
		val=f((i*h))
		values.append(val)

	return values


def eksaktf(x):
	"""
		Den eksakte løsning til differentialligningen f(P0x,P0y)
	"""
	return e**((x**2)/4)

def f(x,y):
	"""
		Differentialligningen f(P0)=f(x,y)=y' som har løsningsfunktionen eksaktf(x)
	"""
	return 0.5*x*y

def eksaktg(x):
	"""
		Den eksakte løsning til differentialligningen g(P1x,P1y)
	"""
	return (((4*x**3)+80)/3)**(1/4)

def g(x,y):
	"""
		Differentialligningen g(P1)=f(x,y) som har løsningsfunktionen eksaktg(x)
	"""
	return (x**2)/(y**3)

P0=(0,1)
P1=(-2,2)
n=25
h=0.1

if __name__ == '__main__':
	print(f'Kvadratsumfejl RK4 tilfælde 1: {beregn_præcision(rk4(f,P0,10,0.1), get_eksakt_values(eksaktf,10,0.1,P0[0]))}')
	print(f'Kvadratsumfejl Euler tilfælde 1: {beregn_præcision(euler(f,P0,10,0.1), get_eksakt_values(eksaktf,10,0.1,P0[0]))}')
	print('\n')
	print(f'Kvadratsumfejl RK4 tilfælde 2: {beregn_præcision(rk4(f,P0,10,0.5), get_eksakt_values(eksaktf,10,0.5,P0[0]))}')
	print(f'Kvadratsumfejl Euler tilfælde 2: {beregn_præcision(euler(f,P0,10,0.5), get_eksakt_values(eksaktf,10,0.5,P0[0]))}')
	print('\n')
	print(f'Kvadratsumfejl RK4 tilfælde 3: {beregn_præcision(rk4(g,P1,25,0.1), get_eksakt_values(eksaktg,25,0.1,P1[0]))}')
	print(f'Kvadratsumfejl Euler tilfælde 3: {beregn_præcision(euler(g,P1,25,0.1), get_eksakt_values(eksaktg,25,0.1,P1[0]))}')
	print('\n')
	print(f'Kvadratsumfejl RK4 tilfælde 4: {beregn_præcision(rk4(g,P1,50,0.1), get_eksakt_values(eksaktg,50,0.1,P1[0]))}')
	print(f'Kvadratsumfejl Euler tilfælde 4: {beregn_præcision(euler(g,P1,50,0.1), get_eksakt_values(eksaktg,50,0.1,P1[0]))}')

	draw_graph([rk4(f,P0,10,0.1),euler(f,P0,10,0.1)],['RK4 af f(x)','EM af f(x)','f(x)'],0.1,P0[0],functions=[eksaktf])	# Tilfælde 1
	draw_graph([rk4(f,P0,10,0.5),euler(f,P0,10,0.5)],['RK4 af f(x)','EM af f(x)','f(x)'],0.5,P0[0],functions=[eksaktf])	# Tilfælde 2
	draw_graph([rk4(g,P1,25,0.1),euler(g,P1,25,0.1)],['RK4 af g(x)','EM af g(x)','g(x)'],0.1,P1[0],functions=[eksaktg]) # Tilfælde 3
	draw_graph([rk4(g,P1,50,0.1),euler(g,P1,50,0.1)],['RK4 af g(x)','EM af g(x)','g(x)'],0.1,P1[0],functions=[eksaktg]) # Tilfælde 4
