#unicode=utf8

from main import *
from math import *


def beregn_præcision(a,b):
	"""
		Beregner den gennemsnitlige overensstemmelse i procent af listen a i forhold til listen b
		Listerne må KUN indeholde floats
	"""
	SS_tot=0		#instansier variabel
	SS_res=0
	shortestlist=None

	if len(a)>len(b):
		shortestlist=b 		# Den korteste liste findes, for at undgå fejl med list index i loop ved gennemløb af liste
	else:
		shortestlist=a

	avg_y_b = sum(b)/len(b)	# Den gennemsnitlige y-værdi af listen b

	for i in range(len(shortestlist)):
		SS_tot+=(a[i]-avg_y_b)**2
		SS_res+=(a[i]-b[i])**2



	accuracy = 1 - (SS_res/SS_tot)
	return accuracy

def get_eksakt_values(f,n,h, P0x):
	"""
		Beregner funktionsværdierne for en funktion f som starter ved x=P0x med n antal iterationer og h stor skridtlængde
	"""
	values=[]
	for i in range(n):
		val=round(f((i*h)+P0x),5)
		values.append(val)

	return values


def eksaktf(x):
	"""
		Den eksakte løsningsfunktion til funktionen f(P0x,P0y)
	"""
	return e**((x**2)/4)

def f(x,y):
	"""
		Differentialligningen f(P0)=f(x,y)=y' som har løsningsfunktionen eksaktf(x)
	"""
	return 0.5*x*y

def eksaktg(x):
	"""
		Den eksakte løsnings til differentialligningen eksaktg(P1x,P1y)
	"""
	return log((x**2*e**2+2)/(2*(e**2)))

def g(x,y):
	"""
		Differentialligningen g(P1)=f(x,y) som har løsningsfunktionen eksaktg(x)
	"""
	return x*e**(-y)

P0=(0,1)
P1=(0,-2)
n=50
h=0.1

if __name__ == '__main__':
	print(f'Gennemsnitlig overensstemmelse mellem RK4 og Eksakt i f er: {beregn_præcision(rk4(f,P0,n,h), get_eksakt_values(eksaktf,n,h,P0[0]))}%')
	print(f'Gennemsnitlig overensstemmelse mellem Eulers metode og Eksakt i f er: {beregn_præcision(euler(f,P0,n,h), get_eksakt_values(eksaktf,n,h,P0[0]))}%')

	print(f'Gennemsnitlig overensstemmelse mellem RK4 og Eksakt i g er: {beregn_præcision(rk4(g,P1,n,h), get_eksakt_values(eksaktg,n,h,P1[0]))}%')
	print(f'Gennemsnitlig overensstemmelse mellem Eulers metode og Eksakt i g er: {beregn_præcision(euler(f,P1,n,h), get_eksakt_values(eksaktg,n,h,P1[0]))}%')

