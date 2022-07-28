from cmath import e
import copy
import random

# For XOR gate
tTable = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0],
]



def sigmoid(x):
    return 1/(1 + e**(-x))
        

def summation(xs, ws, b=0):
    res = 0
    for x, w in zip(xs, ws):
        res += x*w
    return res + b

nodes = [[1, 2], [3, 4], [5]]
w = {}

for i in range(2):
    for l1 in nodes[0 + i]:
        for l2 in nodes[1 + i]:
            key = str(l1) + str(l2)
            w[key] = random.randint(1, 5)/5


b = [random.randint(1, 5)/5 for i in range(3)]

a, epoch = 0.1, 300000
threshold = 0.01
f_in, f_out = {}, {}

print(f'Assigned Value:\nw = {w}\nb ={b}\na = {a}')

for i in range(epoch):
    print(f'\nEpoch: {int(i/10)}')
    sError = 0.0
    w_old = copy.deepcopy(w)
    b_old = b[:]
    
    for row in tTable:
        x = row[:-1]
        inp, out = [], []
        
        inp.append(w['13']*x[0] + w['23']*x[1])
        inp.append(w['14']*x[0] + w['24']*x[1])
        
        for i in inp:
            out.append(sigmoid(i))
        
        inp.append(w['35']*out[0] + w['45']*out[1])
        
        out.append(sigmoid(inp[-1]))
        
        sError += (row[-1] - out[-1])**2
        
        
        predicted, actual = out[-1], row[-1]
        
        d5 = predicted*(1-predicted)*(actual-predicted)
        
        d3 = out[0]*(1-out[0])*d5*w['35']
        d4 = out[1]*(1-out[1])*d5*w['45']
        
        # Updating Bias
        b[0] += b[0] + d3
        b[1] += b[1] + d4
        b[2] += b[2] + d5
        

        delW = {}
        
        # y4 out[1], y3 out[0], UPDATING WEIGHT
        threshold = 0.3
        
        delW['13'] = a*d3*x[0]
        w['13'] += delW['13']
        
        delW['14'] = a*d4*x[0]
        w['14'] += delW['14'] 
        
        delW['23'] = a*d3*x[1]
        w['23'] += delW['23']
        
        delW['24'] = a*d4*x[1]
        w['24'] += delW['24']
        
        delW['35'] = a*d5*out[0]
        w['35'] += delW['35']
        
        delW['45'] = a*d5*out[1]
        w['45'] += delW['45'] 
    
    
    print(f'Out: {out}\nError: {sError}\nw_old: {w_old}\nw_new: {w}\n\n')
    if sError < threshold:
        break
        
        
print('Prediction:\n')


    
for row in tTable:
    x = row[:-1]
    inp, out = [], []
    
    inp.append(w['13']*x[0] + w['23']*x[1])
    inp.append(w['14']*x[0] + w['24']*x[1])
    
    for i in inp:
        out.append(sigmoid(i))
    
    inp.append(w['35']*out[0] + w['45']*out[1])
    
    out.append(sigmoid(inp[-1]))
            
    
    predicted, actual = out[-1], row[-1]
    
    if predicted<0.5:
        predicted = 0
    else:
        predicted = 1
    
    print(predicted)