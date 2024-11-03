# Represents a MaxHeap as an array- while heapify could be by sorting and assuming tree re. indexes (at best O(N*log(N))), the complexity of heapify is O(log(N))
# Yipes- could make a MaxHeap(HashTable) where max heap indexing was composed through probing,
# but I"m not sure that would make any sense [key == index ? yea, consider hashing the index with a list of SystemRandom().randbits -> this will be used for comparison of collisions for probe functions]
# Actually, the heap structure is literally hashing an index, so that resulting index could be hashed, and this combined with a probing function, 
#  would yield a data structure that would certainly be a litle slower than keeping the indexes in order; maybe this would be useful for secure software
#  operation (what buffer one could overwrite would be, at least in part, less predictable, though the references would all still need to work, so it could be made sense of)
#  every aspect of the operation could be hashed and decoded (so some key would need to be secure)
# from pretty_tree import pretty_tree_from_heap


class MaxHeap:
    def __init__(self, name: str =''):
        self.array = self.HeapArray()  # of (priority, item)
        self.last_child = 0
        self.last_parent = 0
        if name == '':
            self.name = self.__repr__()
        else:
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
        if index > 0 and self.array[index][0] > self.array[parent_index][0]:
            self.swap(index, parent_index)
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
        # largest = index
        # left = self.left_child(index)
        # right = self.right_child(index)
        # if self.has_left(index) and self.array[left][0] > self.array[largest][0]:
        #     largest = left
        # if self.has_right(index) and self.array[right][0] > self.array[largest][0]:
        #     largest = right
        # if largest != index:
        #     self.swap(index, largest)
        #     self.percolate_down(largest)

    def push(self, priority, item: any):
        if len(self.array) == 0:
            self.array[0] = (priority, item)
        else:
            self.last_child += 1
            self.array[self.last_child] = (priority, item)
            self.last_parent = self.parent(self.last_child)
            self.percolate_up(self.last_child)  # len(self.array) - 1

    def pop(self):
        self.swap(0, self.last_child)
        popped = self.array.pop(self.last_child)
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

    def display(self) -> None:
        # print pretty tree (MIT) representation of heap (modified to work with a MaxHeap input)
        pretty_tree_from_heap(self)

    class HeapArray(list):
        def __setitem__(self, index: int, value: any) -> None:
            if index >= len(self):
                self.extend([None] * (index - len(self) + 1))
            super().__setitem__(index, value)
        
        # def __getitem__(self, index: int) -> any:
        #     if index >= len(self):
        #         self.extend([None] * (index - len(self) + 1))
        #     super().__getitem__(index)

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 
from max_heap import MaxHeap
# Derived from: https://github.com/joowani/binarytree/blob/master/binarytree/__init__.py
# The following license applies to the TreePrint.py file only.
# MIT License

# Copyright (c) 2016 Joohwan Oh

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# added 11/02/2024 - Alan M H Beem
class TreeNode:
    def __init__(self, node_tuple, left =None, right =None) -> None:
        self.node_tuple = node_tuple
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root) -> None:
        self.root = root


def _array_to_node(input_heap: MaxHeap, index: int) -> TreeNode:
    left = None
    right = None
    if input_heap.has_left(index):
        left = _array_to_node(input_heap, input_heap.left_child(index))
    if input_heap.has_right(index):
        right = _array_to_node(input_heap, input_heap.right_child(index))
    root = TreeNode(input_heap.array[index], left, right)
    return root

def _array_to_tree(input_heap: MaxHeap) -> Tree:
    return Tree(_array_to_node(input_heap, 0))
#
def _pretty_tree_helper(root, curr_index=0):
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    node_repr = str(root.key)

    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = _pretty_tree_helper(root.left, 2 * curr_index + 1)
    r_box, r_box_width, r_root_start, r_root_end = _pretty_tree_helper(root.right, 2 * curr_index + 2)

    # Draw the branch connecting the current root to the left sub-box
    # Pad with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(' ' * (l_root + 1))
        line1.append('_' * (l_box_width - l_root))
        line2.append(' ' * l_root + '/')
        line2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root
    line1.append(node_repr)
    line2.append(' ' * new_root_width)

    # Draw the branch connecting the current root to the right sub-box
    # Pad with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append('_' * r_root)
        line1.append(' ' * (r_box_width - r_root + 1))
        line2.append(' ' * r_root + '\\')
        line2.append(' ' * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = ' ' * gap_size
    new_box = [''.join(line1), ''.join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
        r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root positions
    return new_box, len(new_box[0]), new_root_start, new_root_end

def pretty_tree(tree):
    lines = _pretty_tree_helper(tree.root, 0)[0]
    return '\n' + '\n'.join((line.rstrip() for line in lines))

# added 11/02/2024 - Alan M H Beem
def pretty_tree_from_heap(input_heap: MaxHeap) -> None:
    pretty_tree(_array_to_tree(input_heap))

