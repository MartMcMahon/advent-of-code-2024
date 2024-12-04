import pdb

lines = []
with open("test.txt", "r") as f:
    lines = f.readlines()

count = 0
target = "XMAS"


def check_up():
    for i in range(1, len("XMAS")):
        if lines[max(0, y - i)][x] != target[i]:
            return 0
    return 1


def check_down():
    for i in range(1, len("XMAS")):
        if lines[min(y + i, len(lines) - 1)][x] != target[i]:
            return 0
    return 1


def check_left():
    for i in range(1, len("XMAS")):
        if lines[y][max(0, x - i)] != target[i]:
            return 0
    return 1


def check_right():
    for i in range(1, len("XMAS")):
        if lines[y][min(len(lines[0]) - 1, x + i)] != target[i]:
            return 0
    return 1


def check_upleft():
    for i in range(1, len("XMAS")):
        if lines[max(0, y - i)][max(0, x - i)] != target[i]:
            return 0
    return 1


def check_downleft():
    for i in range(1, len("XMAS")):
        if lines[min(len(lines) - 1, y + i)][max(0, x - i)] != target[i]:
            return 0
    return 1


def check_upright():
    for i in range(1, len("XMAS")):
        if lines[max(0, y - i)][min(len(lines[0]) - 1, x + i)] != target[i]:
            return 0
    return 1


def check_downright():
    for i in range(1, len("XMAS")):
        if (
            lines[min(len(lines) - 1, y + i)][min(len(lines[y]) - 1, x + i)]
            != target[i]
        ):
            return 0
    return 1


for y, line in enumerate(lines):
    for x, c in enumerate(lines[y]):
        # if y == len(lines) - 1:
        #     breakpoint()
        if c == "X":
            if y >= 3:
                count += check_up()
            if y <= len(lines) - 4:
                count += check_down()
            if x >= 3:
                count += check_left()
            if x <= len(lines[0]) - 4:
                count += check_right()
            if y >= 3 and x >= 3:
                count += check_upleft()
            if y <= len(lines) - 4 and x >= 3:
                count += check_downleft()

            if y >= 3 and x <= len(lines[0]) - 4:
                count += check_upright()

            if y <= len(lines) - 4 and x <= len(lines[0]) - 4:
                count += check_downright()
print(count)
