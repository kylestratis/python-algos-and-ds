class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def bubble_up(self, i):
        while i / 2 > 0:
            if self.heap_list[i] < self.heap_list[i/2]:
                self.heap_list[i/2], self.heap_list[i] = self.heap_list[i], self.heap_list[i/2]
            i /= 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.bubble_up(self.current_size)

    def bubble_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delete_min(self):
        ret = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.bubble_down(1)
        return ret

    def build_heap(self, inlist):
        i = len(inlist) / 2
        self.current_size = len(inlist)
        self.heap_list = [0] + inlist[:]
        while i > 0:
            self.bubble_down(i)
            i -= 1