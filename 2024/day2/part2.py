res = 0


def is_safe(report):
    decreasing = int(report[0]) > int(report[1])
    safe = True
    for i in range(len(report) - 1):
        diff = int(report[i]) - int(report[i + 1])
        match = (decreasing and diff > 0) or (not decreasing and not diff > 0)
        if not (abs(diff) < 4 and abs(diff) > 0 and match):
            safe = False
            break
    return safe


with open("./input") as f:
    for line in f:
        safe = 2
        report = line.split()
        if is_safe(report):
            res += 1
            continue
        for i in range(len(report)):
            if is_safe(report[:i] + report[i + 1 :]):
                res += 1
                break

print(res)
