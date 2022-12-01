#PART 1
lines = "".join(list(open("day1data.txt")))
sets = lines.split("\n")

data = [[]]
for i in sets:
    if i == "":
        data.append([])
    else:
        data[-1].append(i)

calorie_bag = [[int(i) for i in lst] for lst in data]

sum_bag = []

for lst in calorie_bag:
    sum_bag.append(sum(lst))
#print(sum_bag.index(max(sum_bag)))
print(max(sum_bag))

#PART 2
sum_bag.sort()
print(sum(sum_bag[-3:]))