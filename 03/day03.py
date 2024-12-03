import re

with open("input.txt", "r") as f:
    input_text = f.read()


def get_muls(do_text):
    print(do_text)
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, do_text)

    sum = 0
    for m in matches:
        s = m.split(",")
        factor1 = int(s[0][4:])
        factor2 = int(s[1][:-1])

        print(m, " = " + str(factor1 * factor2))
        sum += factor1 * factor2
        print("sum is " + str(sum))

    return sum


def dos_and_donts(input_text):
    s1 = input_text.split("do()")
    # s1 = ["do.......dont.......", ..]
    strings = map(lambda x: x.split("don't()")[0], s1)
    # strings = ["do...", ]

    grand_sum = 0
    for s in strings:
        grand_sum += get_muls(s)

    return grand_sum


print(dos_and_donts(input_text))
