#unicode=utf8

import unittest
from main import *
import numpy.testing



geogebra_result=[1.00000000000000,1.00000000000000,1.00500000000000,1.01505000000000,1.03027575000000,1.05088126500000,1.07715329662500,1.10946789552375,1.14829927186708,
	1.19423124274177,1.24797164866515,1.31037023109840,1.38244059380881,1.46538702943734,1.56063718635077,1.66988178939532,1.79512292359997,1.93873275748797,2.10352504187445,
	2.29284229564315,2.51066231372925,2.76172854510217,3.05171004233790,3.38739814699507,3.77694893389950,4.23018280596745,4.75895565671338,5.37761989208612,6.10359857751774,
	6.95810237837023,7.96702722323391,9.16208130671900,10.5822039092604,12.2753565347421,14.3007903629746,16.7319247246802,19.6600115514993,23.1988136307692,27.4905941524615,
	32.7138070414291,39.0929994145078,46.9115992974094,56.5284771533783,68.3994573555878,83.1053406870391,101.388515638188,124.200931656780,152.767145937839,188.667425233232,
	233.947607289207]


def f(P0):
	return 0.5*P0[0]*P0[1]

P0=(0,1)
n=50
h=0.1

if __name__ == '__main__':
	#unittest.main()
	print(numpy.testing.assert_allclose(euler(f,P0,n,h),geogebra_result))
