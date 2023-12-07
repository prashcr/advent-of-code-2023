myfile = open("input.txt", "r")
lines = myfile.readlines()

values = []

max_per_color = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def validate(reveals):
    for reveal in reveals:
        color_counts = reveal.split(", ")
        for color_count in color_counts:
            count, color = color_count.split(" ")
            if int(count) > max_per_color[color]:
                return False
    return True


for line in lines:
    line_start, line_end = line.split(": ")
    game_id = line_start.split(" ")[1]
    reveals = line_end.rstrip().split("; ")
    if validate(reveals):
        values.append(int(game_id))


print(sum(values))
