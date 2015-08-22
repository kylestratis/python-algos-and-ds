# Implementation of BubbleSort

def bubbleSort(unsortedList):
    for passNumber in range(len(unsortedList)):
        for cell in range(len(unsortedList) - 1):
            if unsortedList[cell] > unsortedList[cell + 1]:
                unsortedList[cell], unsortedList[cell + 1] = unsortedList[cell + 1],unsortedList[cell]
    return unsortedList

# Some testing
list = [2, 1, 6, 3, 7, 10]
python = ['p', 'y', 't', 'h', 'o', 'n']
print(list)
print(bubbleSort(list))
print(python)
print(bubbleSort(python))