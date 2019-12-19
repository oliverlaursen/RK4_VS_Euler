#unicode=utf8

from main import *
from math import *


def beregn_præcision(a,b):
	"""
		Beregner kvadratsumfejlen mellem 2 lister.
		
		Listerne må KUN indeholde floats og listerne 
		SKAL indeholde lige mange elementer
	"""
	rkv=0

	for i in range(len(a)):
		rkv+=(a[i]-b[i])**2

	return rkv

def get_eksakt_values(f,n,h, x0):
	"""
		Beregner funktionsværdierne for en funktion f, som starter
		ved x=P0x med n antal iterationer og h stor skridtlængde
	"""
	values=[]
	for i in range(n):
		val=f((i*h)+x0)
		values.append(val)

	return values


def eksaktf(x):
	"""
		Den eksakte løsning til differentialligningen f(0,1)
	"""
	return e**((x**2)/4)

def f(x,y):
	"""
		Differentialligningen f(x,y)=y' som har løsningsfunktionen eksaktf(x)
	"""
	return 0.5*x*y

def eksaktg(x):
	"""
		Den eksakte løsning til differentialligningen g(2,2)
	"""
	return (((4*x**3)+80)/3)**(1/4)

def g(x,y):
	"""
		Differentialligningen g(P1)=f(x,y) som har løsningsfunktionen eksaktg(x)
	"""
	return (x**2)/(y**3)

P0=(0,1)
P1=(-2,2)


if __name__ == '__main__':
	print(f'Kvadratsumfejl RK4 tilfælde 1: {beregn_præcision(rk4(f,P0,25,0.1)[1], get_eksakt_values(eksaktf,25,0.1,P0[0]))}		time = {rk4(f,P0,50,0.1)[0]}')
	print(f'Kvadratsumfejl Euler tilfælde 1: {beregn_præcision(euler(f,P0,25,0.1)[1], get_eksakt_values(eksaktf,25,0.1,P0[0]))}		time = {euler(f,P0,50,0.1)[0]}\n')

	print(f'Kvadratsumfejl RK4 tilfælde 2: {beregn_præcision(rk4(f,P0,25,0.3)[1], get_eksakt_values(eksaktf,25,0.3,P0[0]))}		time = {rk4(f,P0,10,0.5)[0]}')
	print(f'Kvadratsumfejl Euler tilfælde 2: {beregn_præcision(euler(f,P0,25,0.3)[1], get_eksakt_values(eksaktf,25,0.3,P0[0]))}		time = {euler(f,P0,10,0.5)[0]}\n')

	print(f'Kvadratsumfejl RK4 tilfælde 3: {beregn_præcision(rk4(g,P1,25,0.1)[1], get_eksakt_values(eksaktg,25,0.1,P1[0]))}		time = {rk4(f,P0,50,0.1)[0]}')
	print(f'Kvadratsumfejl Euler tilfælde 3: {beregn_præcision(euler(g,P1,25,0.1)[1], get_eksakt_values(eksaktg,25,0.1,P1[0]))}		time = {euler(f,P0,50,0.1)[0]}\n')

	print(f'Kvadratsumfejl RK4 tilfælde 4: {beregn_præcision(rk4(g,P1,25,0.3)[1], get_eksakt_values(eksaktg,25,0.3,P1[0]))}		time = {rk4(f,P0,10,0.5)[0]}')
	print(f'Kvadratsumfejl Euler tilfælde 4: {beregn_præcision(euler(g,P1,25,0.3)[1], get_eksakt_values(eksaktg,25,0.3,P1[0]))}		time = {euler(f,P0,10,0.5)[0]}')

	draw_graph([rk4(f,P0,25,0.1)[1],euler(f,P0,25,0.1)[1]],['RK4 af a(x)','EM af a(x)','a(x)'],0.1,P0[0],functions=[eksaktf])	# Tilfælde 1
	draw_graph([rk4(f,P0,25,0.3)[1],euler(f,P0,25,0.3)[1]],['RK4 af a(x)','EM af a(x)','a(x)'],0.3,P0[0],functions=[eksaktf])	# Tilfælde 2
	draw_graph([rk4(g,P1,25,0.1)[1],euler(g,P1,25,0.1)[1]],['RK4 af b(x)','EM af b(x)','b(x)'],0.1,P1[0],functions=[eksaktg]) # Tilfælde 3
	draw_graph([rk4(g,P1,25,0.3)[1],euler(g,P1,25,0.3)[1]],['RK4 af b(x)','EM af b(x)','b(x)'],0.3,P1[0],functions=[eksaktg]) # Tilfælde 4

