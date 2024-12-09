from collections import defaultdict

res = 0

with open("./input") as f:
    rules, pages = f.read().split("\n\n")

adj = defaultdict(set)
reverse_adj = defaultdict(set)
for rule in rules.splitlines():
    before, after = rule.split("|")
    adj[before].add(after)
    reverse_adj[after].add(before)


def is_ordered(nums):
    for i, n in enumerate(nums):
        for j in range(0, i):
            if n in adj and nums[j] in adj[n]:
                return False

    return True


def top_sort(nums):

    def resolve(n, v, s):
        v[n] = True

        for i in adj[n]:
            if i in v and not v[i]:
                resolve(i, v, s)

        s.append(n)

    visited = {n: False for n in nums}
    stack = []
    end = []
    start = []
    for n in nums:
        if not visited[n]:
            # if n has no afters, it can go to end
            if n not in adj:
                visited[n] = True
                end.append(n)
                continue
            # if nothing has to come before n, it goes to start
            if n not in reverse_adj:
                visited[n] = True
                start.append(n)
                continue
            resolve(n, visited, stack)

    return start + stack[::-1] + end


for page in pages.splitlines():
    nums = page.split(",")
    if not is_ordered(nums):
        s = top_sort(nums)
        res += int(s[len(s) // 2])

print(res)
