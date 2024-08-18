my_list = [1, 2, 3, 4, 5]
reversed_list =[]

i = len(my_list) - 1
while i >= 0:
    reversed_list.append(my_list[i])
    i -= 1

print(reversed_list)