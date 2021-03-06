## Advent of Code -- Day 5 -- Steps
from itertools import chain

steps_input = open("5_py_input.txt", "r")

def listMaker(stepIn):
    counter = 0
    newSteps = []
    steps = []

    for x in stepIn:
        newSteps.append(x)

    for x in newSteps:
        s = int(x.replace('\n', ''))
        steps.append(s)

    return steps

steps = listMaker(steps_input)
test_steps = [0,3,0,1,-3]
#print(steps)

# Func for Part 1

def stepMaker(nlst):
    jump = 0
    i = 0 #index
    steps = 0

    while i < len(nlst): # while index < len(list)
        print(">> NEW", "| list: ", nlst)
        print("i: ",i)
        i += jump
        #print("nlist 1: ", nlst[i])
        jump = nlst[i]
        #print("jump: ", jump)
        nlst[i] += 1
        #print("nlist 2: ",nlst[i])
        steps += 1
        print ("Steps: ", steps)

#stepMaker(steps) #function 1 call

# Func for Part 2
### Takes a long time to get to answer, be patient

def jumpMaker(nlst):
    jump = 0
    i = 0 #index
    steps = 0

    while True: # while index < len(list)
        print(">> NEW","| list: ", nlst)
        print("i: ", i)
        i += jump
        #print("nlist 1: ", nlst[i])
        jump = nlst[i]
        #print("jump: ", jump)

        if jump >= 3:
            nlst[i] -= 1
            #print("larger", "|| nlist 2: ", nlst[i])
        else:
            nlst[i] += 1
            #print("smaller", "|| nlist 2: ", nlst[i])

        steps += 1
        print("Steps: ", steps)


jumpMaker(steps) #function 1 call