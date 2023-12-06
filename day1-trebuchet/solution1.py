myfile = open("input.txt", "r")
lines = myfile.readlines()

values = []

for line in lines:
    first_digit = None
    last_digit = None
    for char in line:
        try:
            int(char)
            if first_digit is None:
                first_digit = char
            last_digit = char
        except:
            next
    values.append(int(first_digit + last_digit))

print(sum(values))
