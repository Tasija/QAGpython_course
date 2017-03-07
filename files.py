limit = 35

with open('test_file.txt') as data_sour, open('new_file.txt', "w") as new_f:
    for line in data_sour:
        if len(line) > limit:
            new_f.write(line)

