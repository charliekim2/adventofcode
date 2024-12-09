dict1 = {}
dict2 = {}

with open("./input") as f:
    for line in f:
        a, b = line.split()
        if a in dict1:
            dict1[a] += 1
        else:
            dict1[a] = 1

        if not a in dict2:
            dict2[a] = 0
        if b in dict2:
            dict2[b] += 1
        else:
            dict2[b] = 1

score = 0
for n in dict1:
    score += int(n) * dict1[n] * dict2[n]

print(score)
