import math

myfile = open("input.txt", "r")
lines = myfile.readlines()

values = []


def power(reveals):
    min_per_color = {}
    for reveal in reveals:
        color_counts = reveal.split(", ")
        for color_count in color_counts:
            count, color = color_count.split(" ")
            if int(count) > min_per_color.get(color, 0):
                min_per_color[color] = int(count)
    return math.prod(min_per_color.values())


for line in lines:
    line_start, line_end = line.split(": ")
    game_id = line_start.split(" ")[1]
    reveals = line_end.rstrip().split("; ")
    values.append(power(reveals))


print(sum(values))
