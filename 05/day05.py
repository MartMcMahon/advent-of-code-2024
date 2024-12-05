import math

reading_rules = True

page_rules_l = []
updates = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        if reading_rules:
            if line == "" or line == "\n":
                reading_rules = False
                continue

            [l, r] = line.split("|")
            l = l.strip()
            r = r.strip()

            page_rules_l.append((l, r))

        else:
            updates.append(line.strip().split(","))


total = 0
for update in updates:
    valid_update = True
    for rule in page_rules_l:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[1]) < update.index(rule[0]):
                valid_update = False
                break
    if valid_update:
        total += int(update[math.floor(len(update) / 2)])


print(total)
