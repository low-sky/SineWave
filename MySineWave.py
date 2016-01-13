import numpy as np
import matplotlib.pyplot as plt

def MySineWave(lam):
	
	#Compute sin(2*pi*x/lambda) from -2*pi to 2*pi
	x = np.arange(-2*np.pi,2*np.pi,0.01)
	f = np.sin(x*2*np.pi/lam)

	#Plot 
	plt.plot(x,f,'g')
	plt.xlim(-2*np.pi,2*np.pi)
	plt.xlabel('x')
	plt.ylabel('$sin(2{\pi}x/%.1f)$' %lam)
	plt.title('Sine Function with Wavelength $\lambda=$%.1f' %lam)
	plt.show()

	return

#Get wavelength from user
#lam = float(input("Enter Wavelength: "))
#MySineWave(lam)
