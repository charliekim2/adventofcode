import re

res = 0
with open("./input") as f:
    for line in f:
        muls = re.findall(r"mul\((\d+)\,(\d+)\)", line)
        for a, b in muls:
            res += int(a) * int(b)

print(res)
