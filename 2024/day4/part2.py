res = 0


def is_xmas(x, y, mat):
    diag1 = mat[y][x] + mat[y + 1][x + 1] + mat[y + 2][x + 2]
    diag2 = mat[y][x + 2] + mat[y + 1][x + 1] + mat[y + 2][x]

    if diag1 + diag2 in ["MASMAS", "SAMSAM", "MASSAM", "SAMMAS"]:
        return 1
    else:
        return 0


with open("./input") as f:
    mat = [list(line) for line in f]
    for i in range(len(mat) - 2):
        for j in range(len(mat[0]) - 2):
            res += is_xmas(j, i, mat)

print(res)
