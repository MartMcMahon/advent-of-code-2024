import math

reading_rules = True

page_rules_l = []
updates = []

rules_order = None

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


part_1_total = 0
p2_total = 0
for update in updates:
    valid_update = True
    for rule in page_rules_l:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[1]) < update.index(rule[0]):
                valid_update = False
                break
    if valid_update:
        part_1_total += int(update[math.floor(len(update) / 2)])
    else:
        page_rules_keys = map(lambda x: x[0], page_rules_l)
        # for update_page_num in update:
        for i in range(len(update)):
            update_page_num = update[i]
            if update_page_num in page_rules_keys:
                page_rules_right = [
                    x[1] for x in page_rules_l if x[0] in page_rules_keys
                ]
                idicies = []
                for right in page_rules_right:
                    if right in update:
                        idx = update.index(right)
                        idicies.append(idx)
                m = min(idicies)
                update = update[:m] + update_page_num


print(p2_total)
