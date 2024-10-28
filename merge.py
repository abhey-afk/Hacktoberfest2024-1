def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Finding the middle of the array
    mid = len(arr) // 2

    # Dividing the elements into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sorting each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merging the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Merge the two halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Collect the remaining elements
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array

# Example usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print("Sorted array is:", sorted_arr)
