import random


# OR gate
tTable = [
    [-1, -1, -1],
    [-1, 1, 1],
    [1, -1, 1],
    [1, 1, 1],
]

w, b = [random.randint(1, 5)/5, random.randint(1, 5)/5], random.randint(1, 5)/5
a, epoch = 0.2, 100
threshold = 0.000000001


print(f'Assigned Value:\nw = {w}, b ={b}\na = {a}')


for i in range(epoch):
    print(f'\nEpoch: {i+1}')
    sError = 0.0
    w_old = w[:]
    b_old = b
    
    for row in tTable:
        actual = row[2]
        x = row[:-1]
        pred_value = x[0]*w[0] + x[1]*w[1] + b
        
        err = actual - pred_value
        
        sError += err**2
        
        w = [w[0]+a*err*x[0], w[1]+a*err*x[1]]
        
        b += a*err
    print(f'Values:\nw = {w} \nb ={b}\na = {a}\nSquared Error = {sError}\n')
    if max([abs(w_old[0] - w[0]), abs(w_old[1] - w[1]), abs(b_old-b)])< threshold:
        break
        
output = []        
        
for row in tTable:
    x = row[:-1]
    pred_value = 1 if (x[0]*w[0] + x[1]*w[1] + b) > 0 else -1
    output.append(pred_value)

print(f'Predicted Output:\n{output}')
    




