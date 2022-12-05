#! /usr/bin/python3
#PART 1
def letter_to_number(x):
    if x == x.lower():
        return ord(x)-96
    else:
        return ord(x)-65+27

priorities = 0

with open("day3data.txt") as file:
	for line in file:
		line = line.strip()
		sack1 = {char for char in line[:len(line) // 2]}
		sack2 = {char for char in line[len(line) // 2 :]}
		priorities += letter_to_number(sack1.intersection(sack2).pop())
print(priorities)

#PART 2
padge_priorities = 0
with open("day3data.txt") as file:
	three_elves = []
	for line in file:
		three_elves.append({letter for letter in line.strip()})
		if len(three_elves) == 3:
			padge_priorities += letter_to_number(three_elves[0].intersection(three_elves[1], three_elves[2]).pop())
			three_elves.clear()
print(padge_priorities)