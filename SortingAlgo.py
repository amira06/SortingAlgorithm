

#create a sorting algorithm that sorts numbers from smallest to largest without the build in sort funtions
original_list = [c, l, y, z, x, o, a, b]
new_list = []

while original_list:
    minimum =original_list[str]
    for a in original_list:
        if a < minimum:
            minimum = a
    new_list.append(minimum)
    original_list.remove(minimum)

print(new_list)
