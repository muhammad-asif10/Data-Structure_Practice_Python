def counting_sort(my_array):
    if not my_array:
        return my_array

    max_value = max(my_array)
    count = [0] * (max_value + 1)
    for value in my_array:
        count[value] += 1

    my_array[:] = []

    for value, freq in enumerate(count):
        my_array.extend([value] * freq)
    return my_array

unsorted_array = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sorted_array = counting_sort(unsorted_array)
print(sorted_array)