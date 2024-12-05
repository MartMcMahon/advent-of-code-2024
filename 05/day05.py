import math

reading_rules = True

page_dict = {}
updates = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        if reading_rules:
            if line == "" or line == "\n":
                reading_rules = False
                continue

            [l, r] = line.split("|")
            l = int(l.strip())
            r = int(r.strip())

            if page_dict.get(l) is None:
                page_dict[l] = {"left": 0, "right": 0}

            if page_dict.get(r) is None:
                page_dict[r] = {"left": 0, "right": 0}

            page_dict[l]["left"] += 1
            page_dict[r]["right"] += 1

        else:
            updates.append([*map(int, line.strip().split(","))])

        page_order = sorted(
            page_dict.keys(), key=lambda x: page_dict[x]["left"], reverse=True
        )

total = 0
for update in updates:
    page_order_idx = 0
    valid_update = True
    for update_page_num in update:
        if update_page_num in page_order[page_order_idx:]:
            page_order_idx = page_order.index(update_page_num)
        else:
            valid_update = False
            break
    if valid_update:
        total += update[math.floor(len(update) / 2)]


print(total)
