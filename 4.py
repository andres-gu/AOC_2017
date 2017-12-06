## Advent of Code -- Day 4 -- High-Entropy Passphrases

phrases_block = open("4_py_input.txt", "r") #file with day 4 input


def phrases_read(ph):
    counter = 0
    for x in range(512):
        line = (ph.readline()).split() #reading input by lines and making a list of the elements separated by spaces
        print("line: ", line, "|| len: ", len(line))

        no_dups = set(line) #new list created w/out duplicates
        print("line2: ", no_dups, "|| len: ", len(no_dups))

        if len(line) == len(no_dups): #comparing previous lists
            counter += 1

    print("Number of valid passphrases: ", counter)


phrases_read(phrases_block)


