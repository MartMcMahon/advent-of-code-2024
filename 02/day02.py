def check_report(report):
    levels = report.split()
    n = len(levels)

    # is_increasing is a misleading name, since we don't actually
    # care if it's true or false, just that it's the same
    is_direction = int(levels[0]) < int(levels[1])
    x = 1
    while x < n:
        if levels[x - 1] == levels[x]:
            return False
        # i miss strict types already. These parentheses tripped me up, beacuse
        # integers can apparently be less than the value False 🙃
        if (int(levels[x - 1]) < int(levels[x])) != is_direction:
            return False
        if abs(int(levels[x]) - int(levels[x - 1])) > 3:
            return False
        x += 1

    return True


with open("input.txt", "r") as f:
    safe_count = 0
    for line in f:
        if check_report(line):
            safe_count += 1

    print(safe_count)
