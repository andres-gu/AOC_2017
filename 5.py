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
print(steps)

# Func for Part 1

def stepMaker(nlst):
    jump = 0
    i = 0 #index
    steps = 0

    while i < len(nlst): # while index < len(list)
        print("i: ",i)
        i += jump
        print("nlist 1: ", nlst[i])
        jump = nlst[i]
        print("jump: ", jump)
        nlst[i] += 1
        print("nlist 2: ",nlst[i])
        steps += 1
        print ("Steps: ", steps)

stepMaker(steps) #function 1 call