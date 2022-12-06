#! /usr/bin/python3
#PART 1
paired_elves = []
in_range = 0
overlap = 0

with open("day4data.txt") as file:
    for line in file:
        line = line.strip()
        tempData = line.split("\n")
        for pair in tempData:
                paired_elves.append(pair.split(","))

def rangeFinder(pair):
    a = pair[0].split("-")
    b = pair[1].split("-")
    return int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1]) or int(b[0]) <= int(a[0]) and int(b[1]) >= int(a[1])

for pair in paired_elves:
    if rangeFinder(pair):
        in_range +=1

print(in_range)

#PART 2

def overlapFinder(pair):
    a = pair[0].split("-")
    b = pair[1].split("-")
    return int(a[0]) <= int(b[1]) and int(a[0]) >= int(b[0]) or int(b[0]) <= int(a[1]) and int(b[0]) >= int(a[0])

for pair in paired_elves:
    if overlapFinder(pair):
        overlap +=1

print(overlap)