## Advent of Code -- Day 4 -- High-Entropy Passphrases

phrases_block = open("4_py_input.txt", "r") #file with day 4 input

# List to be used in second part:
noDups = []

# Part 1
def phrases_read(ph):
    counter = 0
    for x in range(512):
        line = (ph.readline()).split() #reading input by lines and making a list of the elements separated by spaces
        #print("line: ", line, "|| len: ", len(line))

        no_dups = set(line) #new list created w/out duplicates
        #print("line2: ", no_dups, "|| len: ", len(no_dups))

        if len(line) == len(no_dups): #comparing previous lists
            counter += 1
            noDups.append(line) # to use in second part

    print("Number of valid passphrases: ", counter)

phrases_read(phrases_block) #func call


# Part 2
def phrases_anagram(lst):
    counter = 0
    for item in lst:
        s = []
        for x in item:
            r = (sorted(x)) #item letters will be sorted() making easier to compare if anagram is possible
            t = "" #spacer to use when join()
            s.append(t.join(r)) #sorted and joined item to be appended

        no_dups = set(s) #new list w/out duplicates
        #print("len s: ", len(s), "|| len no_dups", len(no_dups))

        if len(s) == len(no_dups): #comparing lists
            counter += 1

    print ("Number of valid and non-anagram passphrases: ", counter)


phrases_anagram(noDups) #func call

