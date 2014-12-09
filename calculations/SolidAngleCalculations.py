from numpy import *
import matplotlib.pyplot as pl

Adet = 0.01**2 # sq centimeter area detector

# 25 mm2 active area and is 500 um thick
Adet = (25e-3)**2

R = linspace(0.01,10,1000)

BK1000nm = 2000.26 * 19.7e-2
MoK = 2561.99
MoL = 4103.36

Omega0 = Adet/R**2

pl.figure()
pl.loglog(R,Omega0)
pl.xlabel(r'X-Ray Path Length $R$ [m]')
pl.ylabel(r'Solid Angle $\Omega$ [Sr]')

LabelBK1000nm = r'B(1$\mu$m)-$K_{\alpha}$ ($0.18$ keV)'
LabelK = r'Mo-$K_{\alpha}$ ($17.4$ keV)'
LabelL = r'Mo-$L$ ($2.3$ keV)'

pl.figure()
pl.loglog(R,BK1000nm*Omega0*1000,label=LabelBK1000nm)
pl.loglog(R,MoK*Omega0*1000,label=LabelK)
pl.loglog(R,MoL*Omega0*1000,'r',label=LabelL)
pl.xlabel(r'X-Ray Path Length $R$ [m]')
pl.ylabel(r'Detected X-Rays [Photons/$\mu$C]')
pl.grid()
pl.legend()

pl.show()

