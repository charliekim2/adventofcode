from collections import defaultdict


# loop if we end up in the same pos and dir as some point before
class Guard:
    def __init__(self, map) -> None:
        self.map = map
        self.set_start()
        self.visited = defaultdict(list)

    def set_start(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                match self.map[i][j]:
                    case "^":
                        self.pos = [j, i]
                        self.dir = [0, -1]
                        return
                    case "v":
                        self.pos = [j, i]
                        self.dir = [0, 1]
                        return
                    case "<":
                        self.pos = [j, i]
                        self.dir = [-1, 0]
                        return
                    case "<":
                        self.pos = [j, i]
                        self.dir = [1, 0]
                        return
                    case _:
                        continue

    def turn_clockwise(self):
        temp_x = self.dir[0]
        self.dir[0] = 0 if self.dir[0] else -1 * self.dir[1]
        self.dir[1] = 0 if self.dir[1] else temp_x

    def is_blocked(self):
        new_x = self.pos[0] + self.dir[0]
        new_y = self.pos[1] + self.dir[1]

        if self.map[new_y][new_x] == "#":
            return True
        return False

    def is_out(self):
        new_x = self.pos[0] + self.dir[0]
        new_y = self.pos[1] + self.dir[1]
        if (
            new_x < 0
            or new_x >= len(self.map[0])
            or new_y < 0
            or new_y >= len(self.map)
        ):
            return True
        return False

    def move(self):
        self.pos[0] += self.dir[0]
        self.pos[1] += self.dir[1]

    def patrol(self):
        self.visited[f"{self.pos[0]} {self.pos[1]}"].append(self.dir[:])
        while True:
            # check if out -> at an edge and face that edge
            if self.is_out():
                return False
            # check if something is in the way, turn if so
            if self.is_blocked():
                self.turn_clockwise()
                continue
            # else move in dir
            self.move()
            # check if loop -> at previous pos in previous dir
            pos_key = f"{self.pos[0]} {self.pos[1]}"
            if pos_key in self.visited and self.dir in self.visited[pos_key]:
                return True
            self.visited[f"{self.pos[0]} {self.pos[1]}"].append(self.dir[:])


if __name__ == "__main__":
    with open("./input") as f:
        map = [list(l.strip()) for l in f]

    g = Guard(map)
    g.patrol()

    res = 0
    for v in g.visited:
        newg = Guard([row[:] for row in map])
        x, y = [int(c) for c in v.split(" ")]
        newg.map[y][x] = "#"
        if newg.patrol():
            res += 1

    print(res)
