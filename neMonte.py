import numpy as np
import matplotlib.pyplot as plt
from random import uniform
import time

d_file = open('neMonte.dat','w+')
start = 10
stop = 100000
_step = 100
exactsolution = 1
x_0 = 0
x_1 = np.pi/2

def monteCarloInt(f_n,a,b, N = 1000000):
    s = 0
    u = a
    for i in np.linspace(x_0,x_1,N):
        s += (f_n(uniform(u,i)))/N
        u = i
    return s

# ly = []
# lx = []
# lt = []

for j in np.arange(start,stop,step=_step):
    # print((x_1-x_0)*monteCarloInt(lambda x:np.cos(x),x_0,x_1,j))
    t_0 = time.time()
    # ly += [(x_1-x_0)monteCarloInt(lambda x: np.cos(x),x_0,x_1,j)]
    # t_1 = time.time()
    # lx += [j]
    # lt += [t_1-t_0]
    d_file.write(f'{j} {(x_1-x_0)*monteCarloInt(lambda x: np.cos(x),x_0,x_1,j)} {time.time()-t_0}\n')

# plt.plot(lx,ly)
# plt.plot(lx,lt)
# # #plt.ylim(0.9,1.15)
# plt.show()