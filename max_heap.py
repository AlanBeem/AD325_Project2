# Represents a MaxHeap as an array- heapify is by sorting and assuming tree re. indexes
# Yipes- could make a MaxHeap(HashTable) where max heap indexing was composed through probing,
# but I"m not sure that would make any sense [key == index ? yea, consider hashing the index with a list of SystemRandom().randbits -> this will be used for comparison of collisions for probe functions]

class MaxHeap:
    def __init__(self, name: str =''):
        self.array = self.HeapArray()  # of (priority, item)
        self.last_child = 0
        self.last_parent = 0
        self.name = name

    def __str__(self) -> str:
        return str(self.array)

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def has_left(self, index):
        left_index = self.left_child(index)
        return left_index <= self.last_child

    def has_right(self, index):
        right_index = self.right_child(index)
        return right_index <= self.last_child
            
    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def percolate_up(self, index):
        parent_index = self.parent(index)
        if self.array[index][0] > self.array[parent_index][0]:
            self.swap(index, parent_index)
            if parent_index > 0:
                self.percolate_up(parent_index)

    def percolate_down(self, index):
        child_indices = (self.left_child(index), self.right_child(index))
        if child_indices[0] <= self.last_child and child_indices[1] <= self.last_child:
            if self.array[child_indices[0]][0] >= self.array[child_indices[1]][0]:
                child_index = child_indices[0]
            else:
                child_index = child_indices[1]
            if self.array[index][0] < self.array[child_index][0]:
                self.swap(index, child_index)
                if child_index <= self.last_parent:
                    self.percolate_down(child_index)  # recursive

    def push(self, priority, item: any):
        if len(self.array) == 0:
            self.array[0] = (priority, item)
        else:
            self.array[self.last_child + 1] = (priority, item)
            self.last_child += 1
            self.last_parent = self.parent(self.last_child)
            self.percolate_up(self.last_child)  # len(self.array) - 1


    def pop(self):
        self.swap(0, self.last_child)
        popped = self.array.pop()
        self.last_child -= 1        #
        self.percolate_down(0)      # bug fix: switched the order of these two lines; else: value of self.last_child invalidates comparison in self.percolate_down(...)  11/01/2024
        return popped

    def top_n(self, n) -> list[any]:
        """will return up to all the items in the heap, and will not raise an exception for n > number of items"""
        top_popped = []
        if n >= len(self.array):
            top_popped = self.array
            self.array = []
        else:
            for t in range(n):
                top_popped.append(self.pop())
        return top_popped

    class HeapArray(list):
        def __setitem__(self, index: int, value: any) -> None:
            # # while index > len(self) - 1:
            # #     self.append(None)
            # for i in range(index + 1 - len(self)):
            #     self.append(None)
            # self[index] = value
            if index >= len(self):
                self.extend([None] * (index - len(self) + 1))
            super().__setitem__(index, value)

