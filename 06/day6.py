with open("test.txt", "r") as f:
    y = 0
    input_map = []
    first_line = f.readline()
    width = len(first_line)

    lines = [first_line] + list(f.readlines())

    for y, line in enumerate(lines):

        start_shape = None
        if "^" in line:
            start_shape = "^"
        elif ">" in line:
            start_shape = ">"
        elif "v" in line:
            start_shape = "v"
        elif "<" in line:
            start_shape = "<"
        start_pos = (line.index(start_shape), y)

x, y = start_pos
while x < width and x > 0 and y < len(lines) and y > 0:
    if lines[y][x] ""
