file = open("day1_input","r")

hodnoty = file.read()
lines = file.readline()
total_lines = len(lines)
cisla_separate = hodnoty.split()
count = 0

elfs = [
    #here add each elf and add his calories to the list
]
    #here calc the elf with most calories
    # using max function find elf with most calories
    #print answer


for elf in hodnoty:
    if cisla_separate == "":
        elfs.append(f"elf{count}")
        count +=1
    else:
        elfs.insert(count, cisla_separate[count])
print(elfs)

    #here define how to seperate data or each elf, after
    #finding a blank line = end of elf1 and make elf2 with empty list