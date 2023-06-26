# this program demonstrates linear regression

import numpy as np
from io import StringIO

input_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
 
def fit_model(input_file):

    para,price = [],[]
    # You can read a CSV file with the function np.genfromtxt(datafile, skip_header=1).
    file1 = np.genfromtxt(input_file, skip_header=1)

    # getting me two different lists of lists to work with
    for i in file1:
        para.append(i[:-1])
        price.append(i[-1])

    # converting to np.arrays to perform further mutliplications
    para = np.array(para)
    price = np.array(price)
    
    # using numpy module To obtain the coefficient estimates
    coeff = np.linalg.lstsq(para, price)[0]

    print(coeff)
    # printing the predicted or "fitted" prices 
    print(para @ coeff)

# simulate reading a file
input_file = StringIO(input_string)
fit_model(input_file)
