class MaxHeap:
    def __init__(self, name: str ='') -> None:
        self.array = []
        if name == '':
            self.name = self.__repr__()
        else:
            self.name = name

    def __str__(self) -> str:
        return f"{self.name}: {str(self.array)}"

    def parent(self, index) -> int:
        return (index - 1) // 2

    def left_child(self, index) -> int:
        return 2 * index + 1

    def right_child(self, index) -> int:
        return 2 * index + 2

    def has_left(self, index) -> bool:
        left_index = self.left_child(index)
        return left_index < len(self.array)

    def has_right(self, index) -> bool:
        right_index = self.right_child(index)
        return right_index < len(self.array)
            
    def swap(self, i, j) -> None:
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def percolate_up(self, index) -> None:
        parent_index = self.parent(index)
        if index > 0 and self.array[index][0] > self.array[parent_index][0]:
            self.swap(index, parent_index)
            self.percolate_up(parent_index)

    def percolate_down(self, index) -> None:
        child_index = index  # largest
        left = self.left_child(index)
        right = self.right_child(index)
        if self.has_left(index) and self.array[left][0] > self.array[child_index][0]:
            child_index = left
        if self.has_right(index) and self.array[right][0] > self.array[child_index][0]:
            child_index = right
        if child_index != index:
            self.swap(index, child_index)
            self.percolate_down(child_index)
        
    def push(self, priority: float, item: any) -> None:
        self.array.append((priority, item))
        self.percolate_up(len(self.array) - 1)

    def pop(self) -> tuple[float, any]:
        if len(self.array) > 1:
            self.swap(0, len(self.array) - 1)
            popped = self.array.pop()
            self.percolate_down(0)
        else:
            popped = self.array.pop()
        return popped

    def top_n(self, n) -> list[tuple[float, any]]:
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

