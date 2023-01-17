import math
import numpy as np

def geometric_mean(input):
    x = np.prod(input)
    res = math.exp(math.log(x)/len(input))
    return res

def mid_range(input):
    return 0.5*(max(input)+min(input))

def harmonic_mean(input):
    divide = np.sum(1/input)
    return len(input)/divide

def lehmer_mean(input,powerRange:tuple):
    f = lambda x : np.sum(input**x)
    return [f(i-1)/f(i) for i in range(powerRange[0],powerRange[1])]
