#! /usr/bin/python3
#PART 1
commands = []
crates = [["N","C","R","T","M","Z","P"],["D","N","T","S","B","Z"],["M","H","Q","R","F","C","T","G"],["G","R","Z"],["Z","N","R","H"],["F","H","S","W","P","Z","L","D"],["W","D","Z","R","C","G","M"],["S","J","F","L","H","W","Z","Q"],["S","Q","P","W","N"]]
top_crates = []

with open("day5data.txt") as file:
    for line in file:
        line = line.replace("move","").replace("from","").replace("to","")
        line = line.strip()
        line = line.split("\n")
        for row in line:
            commands.append(row.split())

for command in commands:
    for i in range(int(command[0])):
        crates[int(command[2])-1].append(crates[int(command[1])-1].pop())

for sub_list in crates:
    top_crates.append(sub_list[-1])

print(top_crates)


