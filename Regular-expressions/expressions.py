import re
#fname = input("Enter file: ")
handle = open("workbook.txt")
numlist = []
for line in handle:
    line = line.rstrip()
    stuff = re.findall(('[0-9]+'), line) #is now a list of numbers (type string) and empty lists
    if len(stuff) < 1: #skips empty lists
        continue
    numlist.append(stuff) #save that info into numlist, numlist is now a list of lists
    flat_list = [] #flattens list of lists into a single list of numbers of type string
    for sublist in numlist:
        for item in sublist:
            flat_list.append(int(item)) #converts from a list of strs to a list of ints
print(sum(flat_list))
