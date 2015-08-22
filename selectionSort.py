# Implementation of Selection Sort

def selection_sort(unsorted_list):
    for pass_num in range(len(unsorted_list)-1, 0, -1):
        highest_pos = 0
        for cell in range(1,pass_num + 1):
            if unsorted_list[cell] > unsorted_list[highest_pos]:
                highest_pos = cell
        unsorted_list[pass_num],unsorted_list[highest_pos] = unsorted_list[highest_pos],unsorted_list[pass_num]
    return unsorted_list

# Test data
list1 = [4, 1, 2, 6, 3, 7, 4]
list2 = [3, 6, 4, 7, 1, 9]

print(list1)
print(selection_sort(list1))
print(list2)
print(selection_sort(list2))