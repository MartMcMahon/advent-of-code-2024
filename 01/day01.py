l1 = []
l2 = []

with open("input.txt", "r") as f:
    for line in f:
        l = line.split()
        if len(l) < 2:
            break
        l1.append(l[0])
        l2.append(l[1])

l1.sort()
l2.sort()

score_map = {}
l2_index = 0

sim_score = 0

for c in range(len(l1)):
    while l2[l2_index] < l1[c]:
        l2_index += 1

    if l2_index >= len(l2):
        break

    if score_map.get(l1[c]) is None:
        # count instances of l1[c]
        instances = 0
        while l2[l2_index] == l1[c]:
            instances += 1
            l2_index += 1
            if l2_index >= len(l2):
                break
        score_map[l1[c]] = instances

    sim_score += int(l1[c]) * int(score_map[l1[c]])


print (sim_score)
