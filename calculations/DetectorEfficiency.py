from numpy import *
import matplotlib.pyplot as pl

Z = [3,4,5,6,7,8,9,10,11,12,13,14]
Element = ('Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si')
C1 = loadtxt('AmptekEfficiency.dat',usecols=[1])
C2 = loadtxt('AmptekEfficiency.dat',usecols=[2])
Be8 = loadtxt('AmptekEfficiency.dat',usecols=[3])
Be12 = loadtxt('AmptekEfficiency.dat',usecols=[4])

#Li	3	0%	29%	0%	0%
#Be	4	0%	13%	0%	0%
#B	5	0.06%	19.7%	0%	0%
#C	6	4.3%	43.9%	0%	0%
#N	7	20.2%	59.2%	0%	0%
#O	8	29.4%	62%	0%	0%
#F	9	46.1%	69%	4%	1%
#Ne	10	58.1%	72.9%	20%	9%
#Na	11	65.4%	75.1%	40%	27%
#Mg	12	70.6%	77.3%	59%	47%
#Al	13	75.4%	80.3%	73%	64%
#Si	14	64.7%	81.8%	82%	75%
MS=8
pl.plot(Z,C2,'o',ms=MS,label='Al/Si$_3$N$_4$ (C2)')
pl.plot(Z,C1,'s',ms=MS,label=r'Al/Si$_3$N$_4$ (C1)')
pl.plot(Z,Be8,'d',ms=MS,label=r'Be (8$\mu$m)')
pl.plot(Z,Be12,'v',ms=MS,label=r'Be (12$\mu$m)')
pl.grid(b=True, which='major')
pl.legend(loc=2)
#pl.xlabel('Atomic number Z')
pl.xlabel('Element')
pl.ylabel('K-shell X-ray detection efficiency  [%]')
pl.xticks(Z,(Element))
pl.xlim(2,15)
pl.show()

