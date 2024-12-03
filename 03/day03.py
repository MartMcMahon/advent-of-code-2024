import re

with open("input.txt", "r") as f:
    input_text = f.read()

pattern = r"mul\(\d+,\d+\)"
matches = re.findall(pattern, input_text)

sum = 0
for m in matches:
    s = m.split(",")
    factor1 = int(s[0][4:])
    factor2 = int(s[1][:-1])

    sum += factor1 * factor2


print(sum)
