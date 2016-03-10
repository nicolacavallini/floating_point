import numpy as np
from math import expm1

D_Sin=[]
for Eps in np.arange(0,20,1):
	D_Sin.append((np.sin(1+(10**-Eps))-np.sin(1))/(10**-Eps))
print D_Sin
