with open("day1_input", "r") as file:
    hodnoty = file.readlines()
count = 0

elfs = [
    #here add each elf and add his calories to the list
]
    #here calc the elf with most calories
    # using max function find elf with most calories
    #print answer
n = "\n"
line = elfs.count(n)
for ciselka in hodnoty:
    if line == '\n':
        elfs.append(f"elf{count}")
        count +=1
    else:
        elfs.insert(count, hodnoty[count])

print(elfs)
    #here define how to seperate data or each elf, after
    #finding a blank line = end of elf1 and make elf2 with empty list