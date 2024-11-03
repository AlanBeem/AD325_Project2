# Represents a MaxHeap as an array- heapify is by sorting and assuming tree re. indexes
# Yipes- could make a MaxHeap(HashTable) where max heap indexing was composed through probing,
# but I"m not sure that would make any sense [key == index ? yea, consider hashing the index with a list of SystemRandom().randbits -> this will be used for comparison of collisions for probe functions]

class MaxHeap:
    def __init__(self, name: str =''):
        # self.array = self.HeapArray()  # of (priority, item)
        self.array = []
        # self.last_child = 0
        # self.last_parent = 0
        if name == '':
            self.name = self.__repr__()
        else:
            self.name = name

    def __str__(self) -> str:
        return f"{self.name}: {str(self.array)}"

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def has_left(self, index):
        left_index = self.left_child(index)
        # return left_index <= self.last_child
        return left_index < len(self.array)

    def has_right(self, index):
        right_index = self.right_child(index)
        # return right_index <= self.last_child
        return right_index < len(self.array)
            
    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def percolate_up(self, index):
        parent_index = self.parent(index)
        if index > 0 and self.array[index][0] > self.array[parent_index][0]:
            self.swap(index, parent_index)
            self.percolate_up(parent_index)

    def percolate_down(self, index):
        child_index = index  # largest
        # print(f"index: {index}")
        # print(f"self.last_child: {self.last_child}")
        # if self.has_left(index) and self.has_right(index):
        #     if self.array[self.left_child(index)] > self.array[self.right_child(index)]:
        #         child_index = self.left_child(index)
        #     else:
        #         child_index = self.right_child(index)
        # else:
        #     if self.has_left(index):
        #         child_index = self.left_child(index)
            # elif self.has_right(index):
            #     child_index = self.right_child(index)
        # child_indices = (self.left_child(index), self.right_child(index))
        # if child_indices[0] <= self.last_child and child_indices[1] <= self.last_child:
        #     if self.array[child_indices[0]][0] >= self.array[child_indices[1]][0]:
        #         child_index = child_indices[0]
        #     else:
        #         child_index = child_indices[1]
        # if len(self.array) > 0:
        #     if self.array[index][0] < self.array[child_index][0]:
        #         self.swap(index, child_index)
        #         self.percolate_down(child_index)  # recursive
        left = self.left_child(index)
        right = self.right_child(index)
        if self.has_left(index) and self.array[left][0] > self.array[child_index][0]:
            child_index = left
        if self.has_right(index) and self.array[right][0] > self.array[child_index][0]:
            child_index = right
        if child_index != index:
            self.swap(index, child_index)
            self.percolate_down(child_index)
        

    def push(self, priority, item: any):
        # if len(self.array) == 0:
        #     self.array[0] = (priority, item)
        # else:
            # self.last_child += 1
            # self.array[self.last_child] = (priority, item)  # this line confusing, HeapArray(list) main utility: displaying None references in tree representation ? agile development ?
            # # self.last_parent = self.parent(self.last_child)
            # self.percolate_up(self.last_child)  # len(self.array) - 1
        self.array.append((priority, item))
        self.percolate_up(len(self.array) - 1)



    def pop(self):
        if len(self.array) > 1:
            # print(f"at call of pop: {self.array}")
            # self.swap(0, self.last_child)
            self.swap(0, len(self.array) - 1)
            # print(f"after swap: {self.array}")
            # popped = self.array.pop(self.last_child)
            popped = self.array.pop()
            # print(f"after pop: {self.array}")
            # self.last_child -= 1        #
            # self.last_child = max(0, self.last_child - 1)
            # print(f"after decrementing last child: {self.array}")
            self.percolate_down(0)      # bug fix: switched the order of these two lines; else: value of self.last_child invalidates comparison in self.percolate_down(...)  11/01/2024
            # print(f"after percolate down: {self.array}")
        else:
            # popped = self.array.pop(self.last_child)
            popped = self.array.pop()
        return popped

    def top_n(self, n) -> list[any]:
        """will return up to all the items in the heap, and will not raise an exception for n > number of items"""
        top_popped = []
        for t in range(min(n, len(self.array))):
            top_popped.append(self.pop())
        return top_popped

    # class HeapArray(list):
    #     def __setitem__(self, index: int, value: any) -> None:
    #         # # while index > len(self) - 1:
    #         # #     self.append(None)
    #         # for i in range(index + 1 - len(self)):
    #         #     self.append(None)
    #         # self[index] = value
    #         if index >= len(self):
    #             self.extend([None] * (index - len(self) + 1))
    #         super().__setitem__(index, value)

