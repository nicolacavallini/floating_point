import numpy as np
import  matplotlib.pyplot as plt

def FD(f,x,h):
	return (f(x+h)-f(x))/h

def main():
	h= np.array([10**(-i) for i in range(1,20)])

	x=1.
	fd =FD(np.sin,x,h)

	error =np.absolute((np.cos(x)-fd))

	plt.loglog(h,error,'-o')
	plt.show()
	return

if __name__ =="__main__":
	main()
