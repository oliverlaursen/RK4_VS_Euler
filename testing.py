#unicode=utf8

from main import *
from math import *


def beregn_præcision(a,b):
	"""
		Beregner den gennemsnitlige overensstemmelse i procent af listen a i forhold til listen b
		Listerne må KUN indeholde floats
	"""
	accuracy=0		#instansier variabel
	shortestlist=None

	if len(a)>len(b):
		shortestlist=b 		# Den korteste liste findes, for at undgå fejl med list index i loop ved gennemløb af liste
	else:
		shortestlist=a

	for i in range(len(shortestlist)):
		acc=100-(abs(a[i]-b[i])/b[i])*100
		accuracy+=acc


	accuracy /= len(shortestlist)
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


def eksakt(x):
	"""
		Den eksakte løsningsfunktion til funktionen f(P0)
	"""
	return e**((x**2)/4)

def f(P0):
	"""
		Differentialligningen f(P0)=f(x,y)=y' som har løsningsfunktionen eksakt(x)
	"""
	return 0.5*P0[0]*P0[1]

P0=(0,1)
n=50
h=0.1

if __name__ == '__main__':
	print(f'Gennemsnitlig overensstemmelse mellem RK4 og Eksakt er: {beregn_præcision(rk4(f,P0,n,h), get_eksakt_values(eksakt,n,h,P0[0]))}%')
	print(f'Gennemsnitlig overensstemmelse mellem Eulers metode og Eksakt er: {beregn_præcision(euler(f,P0,n,h), get_eksakt_values(eksakt,n,h,P0[0]))}%')
