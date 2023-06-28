import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

def sigmoid(i,c1,c2,c3):
    # implementation of the sigmoid function 
    vals = [( i @ c1),(i @ c2), (i @ c3)]
    vals[0] = 1/(1+ math.exp(-vals[0]))
    vals[1] = 1/(1+ math.exp(-vals[1]))
    vals[2] = 1/(1+ math.exp(-vals[2]))

    print(vals.index(max(vals)))

# calculate the output of the sigmoid for x with all three coefficients
sigmoid(x,c1,c2,c3)
