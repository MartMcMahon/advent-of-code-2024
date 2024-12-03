def check_report(levels):
    # levels = report.split()
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
        report = line.split()
        if check_report(report):
            safe_count += 1
        else:
            safe = False
            for idx in range(len(report)):
                report_copy = report.copy()
                report_copy.pop(idx)
                if check_report(report_copy):
                    safe = True

            if safe:
                safe_count += 1

    print(safe_count)
