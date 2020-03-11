import numpy as np
import matplotlib.pyplot as plt
from random import uniform

start = 10
stop = 30000000
_step = 100
exactsolution = 1
x_0 = 0.5
x_1 = np.pi

def monteCarloInt(f_n,a,b, N = 1000000):
    s = 0
    u = a
    for i in np.linspace(x_0,x_1,N):
        s += (f_n(uniform(u,i)))/N
        u = i
    return s

ly = []
lx = []

for j in np.arange(start,stop,step=_step):
    print((x_1-x_0)*monteCarloInt(lambda x: x**(-7)+(x**7)*np.cos(x),x_0,x_1,j))
#     ly += [monteCarloInt(lambda x: x**4,x_0,x_1,j)]
#     lx += [j]

# plt.plot(lx,ly)
# # #plt.ylim(0.9,1.15)
# plt.show()
