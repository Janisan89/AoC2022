#! /usr/bin/python3
#1 point for rock, 2 points for paper, 3 for scissors, 0 for loss, 3 for draw, 6 for victory

#PART 1
my_points = 0
opp_points = 0

lines = "".join(list(open("day2data.txt")))
pairs = lines.split("\n")

for i in pairs:
    if i == "A Y":
        my_points += 8
        opp_points += 1
    elif i == "B Z":
        my_points += 9
        opp_points += 2
    elif i == "C X":
        my_points += 7
        opp_points += 3
    elif i == "A X":
        my_points += 4
        opp_points += 4
    elif i == "B Y":
        my_points += 5
        opp_points += 5
    elif i == "C Z":
        my_points += 6
        opp_points += 6
    elif i == "A Z":
        my_points += 3
        opp_points += 7
    elif i == "B X":
        my_points += 1
        opp_points += 8
    elif i == "C Y":
        my_points += 2
        opp_points += 9
print(my_points)
print(opp_points)

my_real_points = 0
for i in pairs:
    if i == "A X":
        my_real_points += 3
    elif i == "B X":
        my_real_points += 1
    elif i == "C X":
        my_real_points += 2
    elif i == "A Y":
        my_real_points += 4
    elif i == "B Y":
        my_real_points += 5
    elif i == "C Y":
        my_real_points += 6
    elif i == "A Z":
        my_real_points += 8
    elif i == "B Z":
        my_real_points += 9
    elif i == "C Z":
        my_real_points += 7
print(my_real_points)