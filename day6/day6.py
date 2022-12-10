#! /usr/bin/python3
file = open("day6data.txt", "r")
file = file.read()

#PART 1 & 2
part1 = 4
part2 = 14

def signalCounter(file, signal):
    for letter in range(len(file)-(signal-1)):
        counter = file[letter:letter+signal]
        if len(set(counter)) == signal:
            return letter+signal

print(signalCounter(file, part1))
print(signalCounter(file, part2))
