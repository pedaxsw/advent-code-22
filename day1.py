file = open("day1_input", "r")

hodnoty = file.read()
lines = hodnoty.split("\n")  # ["line1", "line2"]
total_lines = len(lines)
cisla_separate = hodnoty.split()

tmp = 0

elfs = [
    # here add each elf and add his calories to the list
]
# here calc the elf with most calories
# using max function find elf with most calories
# print answer


for line in lines:
    if line == "":
        elfs.append(tmp)

        tmp = 0
    else:
        tmp += int(line)

elfs.sort()

print(elfs[-3, -2, -1])

# here define how to seperate data or each elf, after
# finding a blank line = end of elf1 and make elf2 with empty list
