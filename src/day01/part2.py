# run in root dir!
with open("inputs/1", "r") as file:
    lines = file.readlines()

words = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def number_ends(in_string: str):
    # convert words to nums
    for word, digit in words.items():
        if word in in_string:
            in_string = in_string.replace(word, digit)
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
