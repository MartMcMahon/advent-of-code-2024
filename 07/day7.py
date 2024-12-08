total = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        [val, args] = line.split(":")
        val = int(val)
        args = list(map(int, args.strip().split(" ")))

        line_totals = [{args[0]: True}]
        for i in range(1, len(args)):
            line_totals.append({})
            for k in line_totals[i - 1].keys():
                if k + args[i] <= val:
                    line_totals[i][k + args[i]] = True
                if k * args[i] <= val:
                    line_totals[i][k * args[i]] = True
                if int(str(k) + str(args[i])) <= val:
                    line_totals[i][int(str(k) + str(args[i]))] = True

        if val in line_totals[len(args) - 1].keys():
            total += val

print(total)
