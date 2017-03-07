data = [9, 1, 6, 3, 7]
max_n = max(data)
list_of_str = []

for i in data:
    list_of_str.append(('*' * i).rjust(max_n))

matrix = list(zip(*list_of_str))


for r in matrix:
    print("".join(r))


