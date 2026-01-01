def partition(arr, low, high):
    # Choose the rightmost element as pivot
    pivot = arr[high]
    # Pointer for the greater element
    i = low - 1
    # Traverse through all array elements
    for j in range(low, high):
        # If element smaller than pivot is found
        if arr[j] <= pivot:
            # Increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    # Swap the pivot element with the greater element specified by i
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # Return the position from where partition is done
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        # Find the pivot element such that
        # elements smaller than pivot are on the left
        # elements greater than pivot are on the right
        pi = partition(arr, low, high)
        # Recursive call on the left of pivot
        quick_sort(arr, low, pi - 1)
        # Recursive call on the right of pivot
        quick_sort(arr, pi + 1, high)

my_array = [5, 4, 3, 2, 1]
# Initial call should be with the full array range
quick_sort(my_array, 0, len(my_array) - 1)
print(my_array)
