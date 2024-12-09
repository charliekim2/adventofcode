res = 0
orders = {}

with open("./input") as f:
    line = f.readline()
    while line != "\n":
        a, b = line.strip().split("|")
        line = f.readline()
        if b not in orders:
            orders[b] = {a}
        else:
            orders[b].add(a)

    line = f.readline()
    while line:
        wrong = False
        nums = line.strip().split(",")
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if num in orders and nums[j] in orders[num]:
                    wrong = True

        if not wrong:
            res += int(nums[len(nums) // 2])
        line = f.readline()

print(res)
