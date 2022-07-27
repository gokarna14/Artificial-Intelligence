from cmath import inf
import copy

# initial = [
#     [4, 2, 5],
#     [1, 3, 6],
#     [8, 0, 7]
# ]

initial = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

traversedState_ = []
stack = []
costStack = []
minCost = inf


def cost(toCompareMat):
    global goal
    
    result = 0
    for rowIndex in range(len(goal)):
        for columnIndex in range(len(goal[rowIndex])):
            if goal[rowIndex][columnIndex] != toCompareMat[rowIndex][columnIndex]:
                (goalRowIndex, goalColumnIndex) = index_2d(goal, toCompareMat[rowIndex][columnIndex])
                rowChange = abs(goalRowIndex - rowIndex)
                columnChange = abs(goalColumnIndex - columnIndex)
                result += rowChange + columnChange
    return result


def print_matrix(mat, sep = ' '):
    a = [i for i in mat]
    
    while(len(a)<10):
        a.append([
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ])
    for i in zip(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9]): # four possibilities are present 
        for row in i:
            if ' ' not in row:
                print(row, end=sep)      
        print('')


def index_2d(myList, v):
    for i, x in enumerate(myList):  # Find what the hell is this first
        if v in x:
            return i, x.index(v)

def next_steps(mat, p=True, checkAlready =True):
    
    global stack, traversedState_, costStack
    
    if mat in traversedState_ and checkAlready:
        return 'Already traversed'
    if p:
        print('Current Matrix:')
        print_matrix([mat])
    
    traversedState_.append(copy.deepcopy(mat))
    if p:
        print('Next Steps')
    emptyPosition = index_2d(mat, 0)
    result, hs, offsets = [], [], [1, -1, 0]
    orgMat = copy.deepcopy(mat)
    
    for x in offsets:
        for y in offsets:
            if abs(x + y) == 1:
                newX = emptyPosition[0] + x
                newY = emptyPosition[1] + y
                if 0 <= newX <= 2 and  0 <= newY <= 2:
                
                    mat[emptyPosition[0]][emptyPosition[1]] = mat[newX][newY]
                    mat[newX][newY] = 0
                    if mat not in traversedState_ and mat != [
                            [1, 2, 3],
                            [4, 5, 6],
                            [8, 7, 0]
                            ]:
                        result.append(mat)
                        stack.append(mat)
                        c = cost(copy.deepcopy(mat))
                        if p:
                            print(f'Cost: {c}', end='\t')
                        costStack.append(c)
                    
                    mat = copy.deepcopy(orgMat)
    if p:
        print('')
    return result


def check_traversed():
    global initial
    step = 0
    index_ = 0
    temp = []
    for i in range(1, len(traversedState_)+1):
        # print("HERE....")
        lastTraversed = traversedState_[-i:][0]
               
        if initial in next_steps(lastTraversed, False, False):
            print_matrix(temp)
            # print("HERE....2")
            return step
        temp.append(lastTraversed)

    
        
step = 0  
while(initial != goal):
    step += 1
    print(f'\nStep: {step}\n')
    res = next_steps(initial)
    print_matrix(res)
    
    i = costStack.index((min(costStack)))
    temp = costStack.pop(i)
    if temp<minCost:
        minCost = temp
    # print(f'i= {i}')
    
    print(f'Minimum cost till now: {minCost}')
    print(f'Stack size: {len(stack)}')
    
    initial = stack.pop(i)    
    
    
    if step > 40000:
        break
    

print(f'\nTraversed States:')

for matIndex in range(0, len(traversedState_), 10):
    print_matrix(traversedState_[matIndex:matIndex+10])
    print("")
    
print("Finally:")
print_matrix([initial])
    
print(f'\nSummary:\n\tSteps: {step}')
