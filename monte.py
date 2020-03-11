import numpy as np
import matplotlib.pyplot as plt
from random import uniform

start = 10
stop = 1000000
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
    print(monteCarloInt(lambda x:np.cos(x),x_0,x_1,j))