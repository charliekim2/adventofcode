with open("./input") as f:
    list1 = []
    list2 = []

    for line in f:
        a, b = line.split()
        list1.append(int(a))
        list2.append(int(b))

list1.sort()
list2.sort()

res = 0
for i in range(len(list1)):
    res += abs(list1[i] - list2[i])

print(res)
