import math
import numpy as np

def geometric_mean(data):
    x = np.prod(data)
    res = math.exp(math.log(x)/len(data))
    return res

def mid_range(data):
    return 0.5*(max(data)+min(data))

def harmonic_mean(data):
    divide = np.sum(1/data)
    return len(data)/divide

def lehmer_mean(data,powerRange:tuple):
    f = lambda x : np.sum(data**x)
    return [f(i-1)/f(i) for i in range(powerRange[0],powerRange[1])]
