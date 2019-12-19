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


if __name__ == '__main__':
	case_1_rk4=rk4(f,P0,25,0.1)
	case_1_em=euler(f,P0,25,0.1)
	case_2_rk4=rk4(f,P0,25,0.3)
	case_2_em=euler(f,P0,25,0.3)
	case_3_rk4=rk4(g,P1,25,0.1)
	case_3_em=euler(g,P1,25,0.1)
	case_4_rk4=rk4(g,P1,25,0.3)
	case_4_em=euler(g,P1,25,0.3)
	rk4_avg_time=(case_1_rk4[0]+case_2_rk4[0]+case_3_rk4[0]+case_4_rk4[0])/4
	em_avg_time=(case_1_em[0]+case_2_em[0]+case_3_em[0]+case_4_em[0])/4

	print(f'Kvadratsumfejl RK4 tilfælde 1: {beregn_præcision(case_1_rk4[1], get_eksakt_values(eksaktf,25,0.1,P0[0]))}		time = {case_1_rk4[0]}')
	print(f'Kvadratsumfejl Euler tilfælde 1: {beregn_præcision(case_1_em[1], get_eksakt_values(eksaktf,25,0.1,P0[0]))}			time = {case_1_em[0]}\n')

	print(f'Kvadratsumfejl RK4 tilfælde 2: {beregn_præcision(case_2_em[1], get_eksakt_values(eksaktf,25,0.3,P0[0]))}			time = {case_2_rk4[0]}')
	print(f'Kvadratsumfejl Euler tilfælde 2: {beregn_præcision(case_2_rk4[1], get_eksakt_values(eksaktf,25,0.3,P0[0]))}			time = {case_2_em[0]}\n')

	print(f'Kvadratsumfejl RK4 tilfælde 3: {beregn_præcision(case_3_rk4[1], get_eksakt_values(eksaktg,25,0.1,P1[0]))}		time = {case_3_rk4[0]}')
	print(f'Kvadratsumfejl Euler tilfælde 3: {beregn_præcision(case_3_em[1], get_eksakt_values(eksaktg,25,0.1,P1[0]))}		time = {case_3_em[0]}\n')

	print(f'Kvadratsumfejl RK4 tilfælde 4: {beregn_præcision(case_4_rk4[1], get_eksakt_values(eksaktg,25,0.3,P1[0]))}		time = {case_4_rk4[0]}')
	print(f'Kvadratsumfejl Euler tilfælde 4: {beregn_præcision(case_4_em[1], get_eksakt_values(eksaktg,25,0.3,P1[0]))}		time = {case_4_em[0]}\n')

	print(f'RK4 gennemsnit tid = {rk4_avg_time}')
	print(f'EM gennemsnit tid = {em_avg_time}')
	print(f'EM er {rk4_avg_time/em_avg_time} gange hurtigere end RK4')

	draw_graph([case_1_rk4[1],case_1_em[1]],['RK4 af f(x)','EM af f(x)','f(x)'],0.1,P0[0],functions=[eksaktf])	# Tilfælde 1
	draw_graph([case_2_rk4[1],case_2_em[1]],['RK4 af f(x)','EM af f(x)','f(x)'],0.3,P0[0],functions=[eksaktf])	# Tilfælde 2
	draw_graph([case_3_rk4[1],case_3_em[1]],['RK4 af g(x)','EM af g(x)','g(x)'],0.1,P1[0],functions=[eksaktg]) # Tilfælde 3
	draw_graph([case_4_rk4[1],case_4_em[1]],['RK4 af g(x)','EM af g(x)','g(x)'],0.3,P1[0],functions=[eksaktg]) # Tilfælde 4




