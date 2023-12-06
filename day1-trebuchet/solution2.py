import re

myfile = open("input.txt", "r")
lines = myfile.readlines()

digit_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

values = []

for line in lines:
    matches = re.findall(
        "(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))", line
    )
    values.append(int(digit_map[matches[0]] + digit_map[matches[-1]]))

print(sum(values))
