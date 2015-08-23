# Implementation of merge sort

def merge_sort(unsorted_list):
    if len(unsorted_list) > 1:
        midpoint = len(unsorted_list) / 2
        left_half = unsorted_list[0:midpoint]
        right_half = unsorted_list[midpoint:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                unsorted_list[k] = left_half[i]
                i += 1
            else:
                unsorted_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            unsorted_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            unsorted_list[k] = right_half[j]
            j += 1
            k += 1
    return unsorted_list

input_list = [5, 2, 8, 3, 1, 7, 10, 12]
print(input_list)
print(merge_sort(input_list))