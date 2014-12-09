from numpy import *
import matplotlib.pyplot as pp

T = logspace(2,10,1000) # kinetic energy
q0 = 1.6022e-19
c0 = 2.998e8

def KineticEnergyParameters(mc2,T,PlotAll=True):
	gamma = 1.0 + T/(mc2)
	beta = sqrt(1.0 - 1.0/gamma**2)
	p = gamma*(mc2)*beta
	Rb = p /c0# * c0**2# (q0 * c0)
	xlab = 'Kinetic Energy T [eV]'
	if PlotAll==True:
		pp.subplot(2,2,1); pp.loglog(T,beta); pp.ylabel('beta [eV]'); pp.xlabel(xlab)
		pp.subplot(2,2,2); pp.loglog(T,gamma); pp.ylabel('gamma [eV]'); pp.xlabel(xlab)
		pp.subplot(2,2,3); pp.loglog(T,p); pp.ylabel('p [eV/c]'); pp.xlabel(xlab)
		pp.subplot(2,2,4); pp.loglog(T,Rb); pp.ylabel(r'Rigidity [T$\cdot$m]'); pp.xlabel(xlab)
#		pp.subplot(2,2,4); pp.loglog(T,beta*10e-9/2.998*(T+mc2),'--'); pp.ylabel('Rigidity [-]'); pp.xlabel(xlab)
	else:
		pp.loglog(T,Rb); pp.ylabel(r'Rigidity [T$\cdot$m]'); pp.xlabel(xlab)

	return p,beta,gamma,Rb


def TotalEnergyParameters(mc2,T):
	E = logspace(log10(mc2*1.001),log10(max(T)),len(T))
	gamma = E/mc2
	beta = sqrt(1.0 - 1.0/gamma**2)
	p = gamma*(mc2)*beta
	Rb = beta*E/c0
	xlab = 'Total Energy E [eV]'
	pp.subplot(2,2,1); pp.loglog(E,beta); pp.ylabel('beta [eV]'); pp.xlabel(xlab)
	pp.subplot(2,2,2); pp.loglog(E,gamma); pp.ylabel('gamma [eV]'); pp.xlabel(xlab)
	pp.subplot(2,2,3); pp.loglog(E,p); pp.ylabel('p [eV/c]'); pp.xlabel(xlab)
	pp.subplot(2,2,4); pp.loglog(E,Rb); pp.ylabel('Rigidity [T m]'); pp.xlabel(xlab)
	return p,beta,gamma,Rb,E


Me = 0.511e6
Mp = 938e6
Md = 2.0*Mp

pp.figure(1,figsize=(16,10))
KineticEnergyParameters(Me,T);
KineticEnergyParameters(Mp,T);
KineticEnergyParameters(Md,T);
pp.subplot(2,2,1); pp.legend((r'$e^-$',r'$h^+$',r'$d^+$'),loc=1)

pp.figure(2,figsize=(16,10))
TotalEnergyParameters(Me,T);
TotalEnergyParameters(Mp,T);
TotalEnergyParameters(Md,T);
pp.subplot(2,2,1); pp.legend((r'$e^-$',r'$h^+$',r'$d^+$'),loc=1)


pp.figure(3)
KineticEnergyParameters(Me,T,PlotAll=False);
KineticEnergyParameters(Mp,T,PlotAll=False);
KineticEnergyParameters(Md,T,PlotAll=False);
pp.legend((r'$e^-$',r'$h^+$',r'$d^+$'),loc=2)


pp.show()
