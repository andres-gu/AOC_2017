## Advent of Code -- Day 7 -- Recursive Circus
import re, collections
test_input = open("7a_py_input.txt", "r")
test_range = 13
puzzle_input = open("7b_py_input.txt", "r")
puzzle_range = 1059

# Part 1:
def input_corr(inp, krange):
    mList = []
    brList = []
    rootList = []
    rut = []

    for n in range(krange):
        x = inp.readline()
        #print(">> line: ", x)
        search = re.split('\W+', x)
        #print(search)
        search.remove("")
        if len(search) == 2:
            mList.append(search)
        else:
            rt = search.pop(0)
            rootList.append(rt)
            brList.append(search)


    print("mList: ", mList)
    print("brList: ", brList)
    print("rootList: ", rootList)

    for rt in rootList:
        for br in brList:
            if (rt not in br):
                rut.append(rt)

    #print("rut: ", rut)
    response = collections.Counter(rut)
    print(response)

#input_corr(test_input, test_range)
#input_corr(puzzle_input, puzzle_range)


#Part 2

mList = []
brCompList = []
brList = []
br_m_ = []
valueDict = {}

def read_input(inp, krange):
    for n in range(krange):
        x = inp.readline()
        #print(">> line: ", x)
        search = re.split('\W+', x)
        #print(search)
        search.remove("")
        if len(search) == 2:
            mList.append(search)
        else:
            brCompList.append(search)
            brList.append(search[2:])
            br_m_.append(search[:2])

def valueDic():
    nList = mList + br_m_
    #print(nList)
    for x in nList:
        valueDict[x[0]] = int(x[1])

def findBase():
    orderedList = []
    iterable_brList = [item for bList in brList for item in bList]
    for x in br_m_:
        if x[0] not in iterable_brList:
            return brCompList[br_m_.index(x)]
            #print(">> Base found: ", x[0], "| index: ", br_m_.index(x), "| branch: ", brCompList[br_m_.index(x)])

    #print("orderedList: ", orderedList)

def input_calc(i, r):
    read_input(i,r)

    print("length: ", len(mList), "mList: ", mList)
    print("length: ", len(brCompList), "brCompList: ", brCompList)
    print("length: ", len(brList),"brList: ", brList)
    print("length: ", len(br_m_),"br_m_: ", br_m_)

    valueDic()
    print("ValueDict: ", valueDict)

    base = findBase()
    base_r = base[2:]

    print("Base:" , base, base_r)
    list_name = []
    list_numb = []

    for x in base_r:
        #print("1")
        for y in brCompList:
            #print("2")
            if x in y[0]:
                #print("3")
                base_names = [y[0]]
                base_numb = [valueDict[y[0]]]
                branches_names = []
                branches_numb = []
                ls_r = y[2:]
                for n in ls_r:
                    base_names.append(n)
                    base_numb.append(valueDict[n])
                list_name.append(base_names)
                list_numb.append(base_numb)
    #print("list_name", list_name)
    #print("list_numb", list_numb)

    for x in range(len(list_numb)):
        lsum = 0
        for i in list_numb[x]:
            lsum += i

        print("||", list_name[x],list_numb[x], lsum)



    #iterable_brList = [item for bList in brList for item in bList]
    #print("iterable: ", iterable_brList)
    #for x in br_m_:
    #    if x[0] not in iterable_brList:
    #        print("NOT found ", x[0], "index: ", br_m_.index(x), "branch: ", brCompList[br_m_.index(x)])





    #for x in range(len(brList)):
    #    csum = int(br_m_[x][1])
    #    print(br_m_[x][0], "ValueDict: ", csum, "<<<}|")
    #    for i in brList[x]:
    #        csum += valueDict[i]
    #        print("|| ",i, "ValueDict: ", valueDict[i], "Sum1:", csum)




#input_calc(test_input, test_range)
input_calc(puzzle_input, puzzle_range)
