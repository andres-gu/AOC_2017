## Advent of Code -- Day 6 -- Memory Reallocation
b_input = open("6_py_input.txt", "r")

banks = list(map(int,(b_input.readline()).split())) #was read as strings, had to be converted to int
sample_banks = [0,2,7,0]
#print(banks)


def reallocate(bnk):
    bank_comp = []
    cycles = 0
    state = True
    bank = bnk
    max_num = (sorted(bnk))[-1]
    max_index = bnk.index(max_num)

    #while state:


    print("max:", max_num, "|| index: ", max_index)

    bank[max_index] = 0

    index = (max_index + 1)
    numb = max_num
    print("bank:", bank, "|| numb: ", numb, "|| index: ", index)

    for x in range(max_num):
        if index < (len(bank)) and numb <= max_num and numb >= 0:
            bank[index] += 1
            index += 1
            numb -= 1
        else:
            index = 0
            bank[index] += 1
            index += 1
            numb -= 1
            print(".over")

        # for b in range(len(bank)):
        #     if b == idx:
        #         bank[b] = mx % (len(bank) - 1)
        #     else:
        #         bank[b] += dis

        cycles += 1
        print("Bank: ", bank, "|| Cycle: ", cycles)

    x = "".join(map(str, bank))
    if x not in bank_comp:
        bank_comp.append(x)
    elif x in bank_comp:
        state = False
        print("false")

    print("BankComp :", bank_comp)


reallocate(sample_banks)

