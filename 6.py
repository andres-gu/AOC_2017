## Advent of Code -- Day 6 -- Memory Reallocation
b_input = open("6_py_input.txt", "r")

banks = list(map(int,(b_input.readline()).split())) # was read as strings, had to be converted to int
sample_banks = [0,2,7,0]
#print(banks)


# Part 1: Reallocate banks and find the duplicate cycle.
def reallocate(bnk):
    bank_comp = [] #To be used to contain and compare results
    cycles = 0
    state = True
    bank = bnk #Created instance of 'bnk' to keep a copy from modifications

    while state:
        cycles += 1
        max_num = (sorted(bnk))[-1] # maximum number found, used sorted() to get a list with nums from min to max
        max_index = bnk.index(max_num) #use index() and the 'max_num' to get index number in 'bnk' list
        bank[max_index] = 0 #the value in 'bank[index]' needs to be emptied (=0)

        index = (max_index + 1) #iterating index to be used in for-loop
        numb = max_num #control number to be used in for-loop to add the same amount as 'max_num'
        #print("bank:", bank, "|| numb: ", numb, "|| index: ", index)

        for x in range(max_num): #using 'max_num' to control the iterations of additions to be made
            if index < (len(bank)) and numb <= max_num and numb >= 0: #if the index is under the upper limit of list
                bank[index] += 1
                index += 1
                numb -= 1
            else: # if the index goes over the upper limit of list, the index goes to 0 and continues adding
                index = 0
                bank[index] += 1
                index += 1
                numb -= 1

            #print("Bank: ", bank, "|| Cycle: ", cycles)

            print(".") #used to show "processing" in console


        x = "".join(map(str, bank)) #the list 'bank' needs to be converted to string and then joined
        if x not in bank_comp: #checking if the current 'bank' list exists inside the 'bank_comp' list
            bank_comp.append(x)
        elif x in bank_comp: #if current list exists: stop the 'while-loop'
            state = False
            #print("false")
            bank_comp.append(x)

    print("Part 1: >>","Cycles: ", cycles, "|| BankComp :", bank_comp) #results
    return bank_comp


#reallocate(banks)


# Part 2: Find cycles that existed between the repeated instances.
def findCycles(bnk):
    bank_compilation = reallocate(bnk)
    x = bank_compilation[len(bank_compilation)-1]
    sumR = (len(bank_compilation)-1)-bank_compilation.index(x) #results
    print("Part 2: >>","sumR = ", sumR, "|| last_inlist :", x, "|| first_index:", bank_compilation.index(x), "+ last_index:", len(bank_compilation)-1, "|| bank compilation: ", bank_compilation)


findCycles(banks)

