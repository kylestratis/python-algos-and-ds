# Implementation of Insertion Sort

def insertion_sort(unsorted_list):
    for cell in range(1, len(unsorted_list)):
        current_value = unsorted_list[cell]
        current_pos = cell

        while current_pos > 0 and unsorted_list[current_pos-1] > current_value:
            unsorted_list[current_pos],unsorted_list[current_pos-1] = unsorted_list[current_pos-1],unsorted_list[current_pos]
            current_pos -= 1
    return unsorted_list
test_data = [54,26,93,17,77,31,44,55,20]
print(test_data)
print(insertion_sort(test_data))