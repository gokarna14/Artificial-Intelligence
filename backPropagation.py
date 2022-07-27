from cmath import e
from http.client import FOUND
import random

# For OR gate
tTable = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]

def sigmoid(x):
    return 1/(1 + e**(-x))
        

def summation(xs, ws, b=0):
    res = 0
    for x, w in zip(xs, ws):
        res += x*w
    return res + b
 

w, b = [random.randint(1, 5)/5 for i in range(6)], [random.randint(1, 5)/5 for i in range(2)]
a, epoch = 0.2, 5050
threshold = 0.000000001
f_in, f_out = [], []

print(f'Assigned Value:\nw = {w}\nb ={b}\na = {a}')

for i in range(epoch):
    print(f'\nEpoch: {i+1}')
    sError = 0.0
    w_old = w[:]
    b_old = b
    
    for row in tTable:
        f_in, f_out = [], []
        f_in.append(summation(row[:-1], w[0:2], b[0]))
        f_in.append(summation(row[:-1], w[2:4], b[0]))
        for fin in f_in:
            f_out.append(sigmoid(fin))
        f_in.append(summation(f_out, w[4:6], b[1]))
        f_out.append(sigmoid(f_in[-1]))
        
        delta = {}
        delta['f2'] = f_out[-1]*(1-f_out[-1])*(row[-1]-f_out[-1]) 
        delta['f0'] = f_out[0]*(1-f_out[0])*w[4]*delta['f2']
        delta['f1'] = f_out[1]*(1-f_out[1])*w[5]*delta['f2']
        
        
        # updating weights
        w = []
        for wIndex in range(6):
            deltaIndex = "f" + str(int(wIndex/2))
            if wIndex < 4:
                delW = a*delta[deltaIndex]*row[int(wIndex/2)]
            else:
                delW = a*delta[deltaIndex]*f_out[wIndex-4]
            w.append(w_old[wIndex] + delW)
    error = 0
    print(f'w: {w_old}\nFin: {f_in}\nFout: {f_out}\nDelta: {delta}\nw_new: {w}\nError: {error}\n')
    
    
print("Prediction:")

for row in tTable:
    f_in, f_out = [], []
    f_in.append(summation(row[:-1], w[0:2], b[0]))
    f_in.append(summation(row[:-1], w[2:4], b[0]))
    for fin in f_in:
        f_out.append(sigmoid(fin))
    f_in.append(summation(f_out, w[4:6], b[1]))
    f_out.append(sigmoid(f_in[-1]))
    
    print(f'\t{f_out[-1]}')
    