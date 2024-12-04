lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

count = 0
target = "XMAS"


for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[y]) - 1):
        c = lines[y][x]
        if c == "A":
            neighbors = [
                lines[y - 1][x - 1],
                lines[y - 1][x + 1],
                lines[y + 1][x - 1],
                lines[y + 1][x + 1],
            ]
            if (
                neighbors == list("MSMS")
                or neighbors == list("SMSM")
                or neighbors == list("SSMM")
                or neighbors == list("MMSS")
            ):
                count += 1


print(count)
