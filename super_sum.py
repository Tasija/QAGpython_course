
List_of_lists = [[3, 8], 6, 13, [13], [8, 9, [9, 0], 18]]


def super_sum4(list_var):
    all_sum = 0
    for i in list_var:
        if type(i) is list:
            all_sum += super_sum4(i)
        else:
            all_sum += i
    return all_sum


print(super_sum4(List_of_lists))
