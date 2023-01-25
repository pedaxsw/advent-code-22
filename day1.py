with open("day1_input", "r") as file:
    hodnoty = file.read()
    lines = file.readline()
line = lines.split("\n")
cisla = hodnoty.split()
count = 0

elfs = [
    #here add each elf and add his calories to the list
]
    #here calc the elf with most calories
    # using max function find elf with most calories
    #print answer


for elf in cisla:
    if cisla == '\n':
        elfs.append(f"elf{count}")
        count +=1
    else:
        elfs.insert(count, cisla[count])
print(lines)
    #here define how to seperate data or each elf, after
    #finding a blank line = end of elf1 and make elf2 with empty list