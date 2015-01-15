from numpy import *
import matplotlib.pyplot as pl

Adet = 0.01**2 # sq centimeter area detector

# 25 mm2 active area and is 500 um thick
Adet = (25e-3)**2

R = linspace(0.01,10,1000)

BK1000nm = 268.26 * 19.7e-2 *100
MoK = 2635.07
MoL = 4071.73
CrK = 8863.95

Omega0 = Adet/R**2

pl.figure()
pl.loglog(R,Omega0)
pl.xlabel(r'X-Ray Path Length $R$ [m]')
pl.ylabel(r'Solid Angle $\Omega$ [Sr]')

LabelBK100nm = r'B(100nm)-$K_{\alpha}$ [$0.18$ keV]'
LabelK = r'Mo-$K_{\alpha}$ [$17.4$ keV]'
LabelL = r'Mo-$L$ [$2.3$ keV]'
LabelCrK = r'Cr-$K$ (under Mo(500nm)) [6.0 keV]'

pl.figure()
pl.loglog(R,CrK*Omega0*1000,'k',label=LabelCrK)
pl.loglog(R,BK1000nm*Omega0*1000,label=LabelBK100nm)
pl.loglog(R,MoL*Omega0*1000,'r',label=LabelL)
pl.loglog(R,MoK*Omega0*1000,label=LabelK)
pl.xlabel(r'X-Ray Path Length $R$ [m]')
pl.ylabel(r'Detected X-Rays [Photons/$\mu$C]')
pl.title('Detected X-Rays for 25mm$^2$ Amptek SDD detector')  
pl.grid()
pl.legend()

pl.show()

