# Implementation of BubbleSort

def bubble_sort(unsorted_list):
    for pass_number in range(len(unsorted_list)):
        for cell in range(len(unsorted_list) - 1):
            if unsorted_list[cell] > unsorted_list[cell + 1]:
                unsorted_list[cell], unsorted_list[cell + 1] = unsorted_list[cell + 1],unsorted_list[cell]
    return unsorted_list

# Some testing
list = [2, 1, 6, 3, 7, 10]
list2 = [10, 1, 4, 5, 2, 6]
python = ['p', 'y', 't', 'h', 'o', 'n']
print(list)
print(bubble_sort(list))
print(python)
print(bubble_sort(python))
print(list2)
print(bubble_sort(list2))