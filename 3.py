## Advent of Code -- Day 3 -- Spiral Memory

import itertools

# given input number
exitNum = 347991

# test input numbers
testNum = 10
testNum2 = 63

## Part 1 : Spiral-Pattern Grid + Manhattan Distance Calculation

# Spiral Grid Creation:
# 'step' Functions to modify position coordinates (helper funcs)
def sRight(x,y):
    return x+1, y
def sUp(x,y):
    return x, y+1
def sLeft(x,y):
    return x-1, y
def sDown(x,y):
    return x, y-1

# List of 'steps' functions, later to be iterated through w/ itertools.cycle
steps = [sRight, sUp, sLeft, sDown]

# Function to create grid (main func)
def gridMk(eStop):
    # Iteration of 'steps' list.
    stepsR = itertools.cycle(steps)
    x = 1
    loc = 0,0
    tx = 1

    # access port / starting point creation:
    yield x, loc
    #print("x: ", x,"loc: ", loc)

    while True:
        # range(2): every 2 movements, the steps need to increase by 1
        for t in range(2):
            step = next(stepsR)
            for r in range(tx):
                if x >= eStop:
                    return
                loc = step(loc[0],loc[1])
                x += 1
                yield x, loc
        tx += 1


# x = list(gridMk(exitNum))
# print("first: ", x[0], "|| last: ",x[-1])
# sumR = -(x[0][1][0] + x[-1][1][0])+(x[0][1][1] + x[-1][1][1])
# print (sumR)


## Part 2 : Spiral-Pattern value addition

# 8 functions to map cells around square (helper funcs)
def c1(x,y):
    return x-1, y+1
def c2(x,y):
    return x, y+1
def c3(x,y):
    return x+1, y+1
def c4(x,y):
    return x+1, y
def c5(x,y):
    return x+1, y-1
def c6(x,y):
    return x, y-1
def c7(x,y):
    return x-1, y-1
def c8(x,y):
    return x-1, y
# list to be cycled through
cs = [c1, c2, c3, c4, c5, c6, c7, c8]

# adjacent squares Sum Function (main func)
def calcG(lst):
    struct = lst #list to be used as a template for new dictionary
    pNums = 8 #number of adjacent cells
    cs_ = itertools.cycle(cs)
    newDict = {(0,0):1} #new dictionary w/ first cell initialized

    for s in range(1,len(struct)):
        addit = 0
        x = struct[s][1][0]
        y = struct[s][1][1]
        for i in range(pNums):
            c = next(cs_)
            loc = c(x,y)
            if loc not in newDict:
                addit += 0
            else:
                addit += newDict[loc]

        newDict[(x,y)] = addit
        print("+++ addit: ", addit, "|| newDict: ", newDict)


gc = list(gridMk(testNum2)) #list needed for calcG()
calcG(gc)