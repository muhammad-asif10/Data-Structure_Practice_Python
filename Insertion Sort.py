my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1, n):
    insert_index = i
    cuurent_value = my_array[insert_index]
    for j in range(i-1, -1, -1):
        if my_array[j] > cuurent_value:
            my_array[j + 1] = my_array[j]
            insert_index = j
        else:
            break
    my_array[insert_index]= cuurent_value

print("Sorted Array:", my_array)