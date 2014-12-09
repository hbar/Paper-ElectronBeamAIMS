from numpy import *
import pylab as pl

Energy = linspace(0.5e3, 50e3, 1000)

Label = ['B', 'Mo', 'W']
Rho = [2.35, 10.28, 19.25] # gram/cm^3
Z = [5,42,74]
A = [10.811, 95.95, 183.84]
C = ['b','g','r']
Range = []
RangeAve = []

for i in range(len(Rho)):
	rho = Rho[i] * 1e6 #micrograms/cm^3
	Rex = 1.294e-4 * Energy**1.492 * (A[i]/Z[i]) # micrograms/cm^2
	R50 = 0.3655 * Rex**1.024
	Range.append(Rex / rho * 1e-2 )
	RangeAve.append(R50 / rho * 1e-2 )

pl.figure()
for i in range(len(Rho)):
	pl.plot(Energy*1e-3,Range[i]*1e6,color=C[i],linestyle='--',label = Label[i] + ' Extrapolated Range')
for i in range(len(Rho)):
	pl.plot(Energy*1e-3,RangeAve[i]*1e6,color=C[i],label = Label[i] + ' Median Range')

pl.figure(1); pl.xlabel('Energy [keV]'); pl.ylabel(r'Range [$\mu$m]'); pl.legend(loc=2)
pl.title('Electron beam range in solid targets'); pl.ylim(0,10)
pl.show()

