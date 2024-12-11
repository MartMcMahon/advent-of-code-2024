import pdb

DIRS = [(-1, 0), (0, +1), (+1, 0), (0, -1)]


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.val = 0
        self.path_count = 0
        self.is_calced = False
        self.is_nine = False

    def __repr__(self):
        return f"({self.x},{self.y}) {self.val} \n"

    def coords(self):
        return self.x, self.y

    def calc(self, map):
        if self.is_calced:
            print(
                f"Returning cached result for ({self.x}, {self.y}) -> {self.path_count}"
            )
            return self.path_count
        if self.val == 9:
            print(f"Reached 9 at ({self.x}, {self.y})")
            self.is_calced = True
            return 1

        self.is_calced = True
        total = 0

        # check up
        if self.y > 0:
            if map[self.y - 1][self.x].val == self.val + 1:
                if map[self.y - 1][self.x].is_calced:
                    total += map[self.y - 1][self.x].path_count
                else:
                    total += map[self.y - 1][self.x].calc(map)

        # check right
        if self.x < WIDTH - 1:
            if map[self.y][self.x + 1].val == self.val + 1:
                if map[self.y][self.x + 1].is_calced:
                    total += map[self.y][self.x + 1].path_count
                else:
                    total += map[self.y][self.x + 1].calc(map)

        # check down
        if self.y < HEIGHT - 1:
            if map[self.y + 1][self.x].val == self.val + 1:
                if map[self.y + 1][self.x].is_calced:
                    total += map[self.y + 1][self.x].path_count
                else:
                    if map[self.y + 1][self.x].val == self.val + 1:
                        total += map[self.y + 1][self.x].calc(map)
        # check left
        if self.x > 0:
            if map[self.y][self.x - 1].val == self.val + 1:
                if map[self.y][self.x - 1].is_calced:
                    total += map[self.y][self.x - 1].path_count
                else:
                    total += map[self.y][self.x - 1].calc(map)

        ## # save total in path_count and set flag
        print(f"Total paths from ({self.x}, {self.y}) -> {total}")
        self.path_count = total
        return total


input_text = [[]]
trail_map = [[]]
with open("test.txt", "r") as f:
    y = 0
    x = 0
    for c in f.read():
        if c == "\n":
            x = 0
            y += 1
            input_text.append([])
            trail_map.append([])
            continue
        input_text[y].append(c)
        # breakpoint()
        n = Node(x, y)
        n.val = int(c)

        trail_map[y].append(n)
        x += 1

    input_text = input_text[:-1]
    trail_map = trail_map[:-1]

HEIGHT = len(trail_map)
WIDTH = len(trail_map[0])

total = 0
for line in trail_map:
    for n in line:
        x, y = n.coords()
        if n.val == 0:
            total += n.calc(trail_map)

print(total)
