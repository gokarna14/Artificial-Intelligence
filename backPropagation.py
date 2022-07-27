from cmath import e
import random

# OR gate
tTable = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]

def sigmoid(x):
    return 1/(1 + e**(-x))
        

def summation(xs, ws, b):
    res = 0
    for x, w in zip(xs, ws):
        res += x*w
    return res
 

w, b = [random.randint(1, 5)/5 for i in range(6)], [random.randint(1, 5)/5 for i in range(2)]
a, epoch = 0.2, 1
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
        f_in.append(summation(f_out, w[4:5], b[1]))
        f_out.append(sigmoid(f_in[-1]))
        
        error = ((row[-1] - sigmoid(f_out[-1]))**2)/2
        delta = abs(f_in[-1] - f_out[-1])
        
        print(f'Fin: {f_in}\nFout: {f_out}\nDelta: {delta}\nError: {error}\n')
    
    
    