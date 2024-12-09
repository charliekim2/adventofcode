res = 0
with open("./input") as f:
    for line in f:
        report = line.split()
        decreasing = int(report[0]) > int(report[1])
        safe = True
        for i in range(len(report) - 1):
            diff = int(report[i]) - int(report[i + 1])
            match = (decreasing and diff > 0) or (not decreasing and not diff > 0)
            if not (abs(diff) < 4 and abs(diff) > 0 and match):
                safe = False
                break

        if safe:
            print(line)
            res += 1

print(res)
