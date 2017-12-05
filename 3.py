import itertools
exitNum = 347991
testNum = 10


# steps
def sRight(x,y):
    return x+1, y
def sUp(x,y):
    return x, y+1
def sLeft(x,y):
    return x-1, y
def sDown(x,y):
    return x, y-1
steps = [sRight, sUp, sLeft, sDown]

def gridMk(eStop):
    stepsR = itertools.cycle(steps)
    x = 1
    loc = 0,0
    tx = 1

    yield x, loc
    print("x: ", x,"loc: ", loc)

    while True:
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


def gridCalc(eStop):
    stepsR = itertools.cycle(steps)
    x = 1
    loc = 0,0
    tx = 1

    yield x, loc
    #print("x: ", x,"loc: ", loc)
    while True:
        for t in range(2):
            step = next(stepsR)
            for r in range(tx):
                if x >= eStop:
                    return
                loc = step(loc[0],loc[1])
                x += 1
                yield x, loc
        tx += 1




gc = list(gridCalc(testNum))
spiralDict = {}
for n in range(len(gc)):
    spiralDict[gc[n][1]] = gc[n][0]
print("SpiralDict: ", spiralDict)



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

cs = [c1, c2, c3, c4, c5, c6, c7, c8]

def nStruct(lst):
    nStructLst = []
    for item in range(len(lst)):
        nStructLst.append((0,lst[item][1]))
    print(nStructLst)

def calcG(lst):
    struct = lst
    print(struct)
    pNums = 8
    counter = 0
    cs_ = itertools.cycle(cs)
    newStruct = []
    newDict = {(0,0):1}



    for s in struct:
        #print(s)
        addit = 0
        for i in range(pNums):
            c = next(cs_)
            x = struct[counter][1][0]
            y = struct[counter][1][1]
            loc = c(x,y)
            if loc not in spiralDict:
                addit += 0
            elif spiralDict[loc] <= s[0]:
                print("yep", spiralDict[loc])
                addit += spiralDict[loc]

            print("s:", s,"|| i: ", i,"|| x: ", x, "|| y: ", y, "|| loc: ", loc)
        print(addit)
        counter += 1

nStruct(gc)
calcG(gc)

# def calcGrid(n):
#
#     struct = spiralDict
#     struct[(0,0)] = 1
#     print ("struct", struct)
#
#     i = 2
#     print("s-i ",struct[i])
#     while True:
#         x,y = struct[i]
#         t = 0
#         for rx in range(-1, 2):
#             for ry in range(-1, 2):
#                 rc = (x + rx, y + ry)
#                 if rc in struct:
#                     t += struct[rc]
#         if t > n:
#             return t
#         struct[(x,y)] = t
#         i += 1
#
#         print("struct ", struct)
#
# calcGrid(testNum)
