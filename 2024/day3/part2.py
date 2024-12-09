import re

res = 0

with open("./input") as f:
    enable = True
    for line in f:
        matches = re.findall(r"mul\((\d+)\,(\d+)\)|(do\(\))|(don\'t\(\))", line)
        for a, b, do, dont in matches:
            if do:
                enable = True
            if dont:
                enable = False
            if enable and a and b:
                res += int(a) * int(b)

print(res)
