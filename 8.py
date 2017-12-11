## Advent of Code -- Day 8 -- I Heard You Like Registers
from re import search

test_input = open("8a_py_input.txt", "r")
test_range = 4
register_input = open("8b_py_input.txt", "r")
register_range = 1000



def input_maker(i, n): #takes input and makes a list
    lst = []
    for v in range(n):
        lst.append(i.readline().split())
    return lst

def initial_values(lst): #creates a dictionary ignoring repeated keys
    initial_vals = {}

    for x in lst:
        if x[0] not in initial_vals:
            initial_vals[x[0]] = 0
    return initial_vals

# • Part 1 - compares the operators and makes an operation on the dictionary to get the maximum number.
# • Part 2 - at the beginning of the for-loop, the maximum number in the dictionary from the previous loop is appended to
#   max_list[] to later return maximum number from dictionary of registries.

def logic(a,b):
    max_list = []
    for x in a:
        max_list.append(max(in_values.values()))
        if x[5] == '>':
            if b[x[4]] > int(x[6]):
                if x[1] == 'inc':
                    b[x[0]] += int(x[2])
                else:
                    b[x[0]] -= int(x[2])
        elif x[5] == '<':
            if b[x[4]] < int(x[6]):
                if x[1] == 'inc':
                    b[x[0]] += int(x[2])
                else:
                    b[x[0]] -= int(x[2])
        elif x[5] == '>=':
            if b[x[4]] >= int(x[6]):
                if x[1] == 'inc':
                    b[x[0]] += int(x[2])
                else:
                    b[x[0]] -= int(x[2])
        elif x[5] == '<=':
            if b[x[4]] <= int(x[6]):
                if x[1] == 'inc':
                    b[x[0]] += int(x[2])
                else:
                    b[x[0]] -= int(x[2])
        elif x[5] == '!=':
            if b[x[4]] != int(x[6]):
                if x[1] == 'inc':
                    b[x[0]] += int(x[2])
                else:
                    b[x[0]] -= int(x[2])
        elif x[5] == '==':
            if b[x[4]] == int(x[6]):
                if x[1] == 'inc':
                    b[x[0]] += int(x[2])
                else:
                    b[x[0]] -= int(x[2])
        else:
            print("nope")

    return max(max_list)

#read_input = input_maker(test_input, test_range)
read_input = input_maker(register_input, register_range)

in_values = initial_values(read_input)
mem_alloc = logic(read_input, in_values)

print("maximum number: ", max(in_values.values()))
print("maximum memory alloc.: ", mem_alloc)
