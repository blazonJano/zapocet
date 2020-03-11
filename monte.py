import numpy as np
import matplotlib.pyplot as plt
from random import uniform
import time

d_file = open('Monte.dat','w+')
start = 10
stop = 100000
_step = 100
exactsolution = 1
x_0 = 0
x_1 = np.pi/2

def monteCarloInt(f_n,a,b, N = 1000000):
    s = 0
    for _ in range(N):
        x = uniform(a,b)
        y = uniform(a,b)
        if y <= f_n(x):
            s += 1
    return (b-a)**2*s/(N)

for j in np.arange(start,stop,step=_step):
    t_0 = time.time()
    # print(monteCarloInt(lambda x:np.cos(x),x_0,x_1,j))
    d_file.write(f'{j} {monteCarloInt(lambda x: np.cos(x),x_0,x_1,j)} {time.time()-t_0}\n')