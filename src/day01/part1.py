# run in root dir!
with open("inputs/1", "r") as file:
    lines = file.readlines()


def number_ends(in_string):
    for char in in_string:
        if char.isdigit():
            first = char
            break
    for char in reversed(in_string):
        if char.isdigit():
            last = char
            break
    return int(first + last)


total = 0
for line in lines:
    total += number_ends(line)

print(total)
