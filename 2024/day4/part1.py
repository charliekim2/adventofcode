res = 0


def xmas(x, y, mat):
    h = len(mat)
    w = len(mat[0])

    count = 0
    if mat[y][x] != "X":
        return count
    if x - 3 >= 0:
        s = mat[y][x - 1] + mat[y][x - 2] + mat[y][x - 3]
        if s == "MAS":
            count += 1
    if x + 3 < w:
        s = mat[y][x + 1] + mat[y][x + 2] + mat[y][x + 3]
        if s == "MAS":
            count += 1
    if y - 3 >= 0:
        s = mat[y - 1][x] + mat[y - 2][x] + mat[y - 3][x]
        if s == "MAS":
            count += 1
        if x - 3 >= 0:
            s = mat[y - 1][x - 1] + mat[y - 2][x - 2] + mat[y - 3][x - 3]
            if s == "MAS":
                count += 1
        if x + 3 < w:
            s = mat[y - 1][x + 1] + mat[y - 2][x + 2] + mat[y - 3][x + 3]
            if s == "MAS":
                count += 1
    if y + 3 < h:
        s = mat[y + 1][x] + mat[y + 2][x] + mat[y + 3][x]
        if s == "MAS":
            count += 1
        if x - 3 >= 0:
            s = mat[y + 1][x - 1] + mat[y + 2][x - 2] + mat[y + 3][x - 3]
            if s == "MAS":
                count += 1
        if x + 3 < w:
            s = mat[y + 1][x + 1] + mat[y + 2][x + 2] + mat[y + 3][x + 3]
            if s == "MAS":
                count += 1
    return count


with open("./input") as f:
    mat = [list(line) for line in f]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            res += xmas(j, i, mat)
print(res)
