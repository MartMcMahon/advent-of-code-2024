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

diff = 0
for c in range(len(l1)):
    if l1[c] > l2[c]:
        diff += int(l1[c]) - int(l2[c])
    else:
        diff += int(l2[c]) - int(l1[c])


print (diff)
