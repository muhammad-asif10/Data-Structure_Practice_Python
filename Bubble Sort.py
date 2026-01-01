my_array = [2,5,3,6,4,8,10,9,7,11,14,13,12]

n = len(my_array)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j],my_array[j+1] = my_array[j+1],my_array[j]
            swapped = True
    if not swapped:
        break

print("Sorted Array: ",my_array)