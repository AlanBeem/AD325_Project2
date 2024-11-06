from max_heap import MaxHeap


class UserMaxHeap(MaxHeap):
    # same except updates values by two techniques: 1) maximum, 2) sum
    def __init__(self, name: str ='', update_technique: str ='max') -> None:                      # differences from super
        super().__init__(name)
        self.update_technique = update_technique                                                  #
    
    def push(self, priority: float, item: any) -> None:
        if len(self.array) == 0:
            # self.array[0] = (priority, item)
            self.array.append((priority, item))
        else:
            ## BUG: inconsistent results for keep maximum technique
            ## late solution: modify in place and percolate up
            for index in range(len(self.array)):
                if self.array[index][1] == item:
                    if self.update_technique == 'sum':
                        self.array[index] = (self.array[index][0] + priority, item)
                    elif self.update_technique == 'max':
                        self.array[index] = (max(round(self.array[index][0], 4), round(priority, 4)), item)
                    self.percolate_up(index)
                    # self.percolate_down(0)
                    break
            # tuples are not heaped by item value at all, but by priority, therefore linear search#
            # traverses array, finds value, pops value to update, updates and inserts value         #
            # update_bool = False                                                                   #
            # array_was = self.array.copy()
            # array_range = list(range(len(self.array)))
            # for each_tuple, index in zip(self.array, range(len(self.array))):                     # 
            #     # print(each_tuple)
            #     if each_tuple[1] == item:                                                         #
            #         # print(f"entered condition for each_tuple[1] == item: item: {item}, each_tuple[1]: {each_tuple[1]}")
            #         was_tuple = self.pop(index)
            #         # update_bool = True                                                            #
            #         if self.update_technique.lower() == 'sum':                                    #
            #             # self.array[index] = (priority + self.array[index][0], item)               ##  this update likely violates the heap property
            #             # self.percolate_up(index)
            #             # self.percolate_down(0)
            #             priority = priority + was_tuple[0]
            #         elif self.update_technique.lower().startswith('max'):                         #
            #             # self.array[index] = (max(priority, self.array[index][0]), item)           ##
            #             # self.percolate_up(index)
            #             # self.percolate_down(0)
            #             priority = max(priority, was_tuple[0])
            #         break                                                                         #
            # if not update_bool:
            super().push(priority, item)
    
    def pop(self, index: int =0) -> tuple[float, any]:                                                                 #
        if len(self.array) > 1:
        # print(f"index: {index}")
        # print(f"self.last_child: {self.last_child}")
        # print(f"len(self.array): {len(self.array)}")
        # self.swap(index, self.last_child)                                                         #
            self.swap(index, len(self.array) - 1)
            popped = self.array.pop()
        # self.last_child -= 1
        # self.last_child = max(0, self.last_child - 1)
        # self.last_child = len(self.array) - 1
            self.percolate_down(index)
        else:
            popped = self.array.pop()
        return popped
    
    # def display(self) -> None:
    #     pretty_tree_from_heap(self)
    
# ######################################################
# # Derived from: https://github.com/joowani/binarytree/blob/master/binarytree/__init__.py
# # The following license applies to the TreePrint.py file only.
# # MIT License

# # Copyright (c) 2016 Joohwan Oh

# # Permission is hereby granted, free of charge, to any person obtaining a copy
# # of this software and associated documentation files (the "Software"), to deal
# # in the Software without restriction, including without limitation the rights
# # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# # copies of the Software, and to permit persons to whom the Software is
# # furnished to do so, subject to the following conditions:

# # The above copyright notice and this permission notice shall be included in all
# # copies or substantial portions of the Software.

# # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# # SOFTWARE.

# # added 11/02/2024 - Alan M H Beem
# class TreeNode:
#     def __init__(self, node_tuple, left =None, right =None) -> None:
#         self.node_tuple = node_tuple
#         self.key = node_tuple[0]
#         self.value = node_tuple[1]
#         self.left = left
#         self.right = right


# class Tree:
#     def __init__(self, root) -> None:
#         self.root = root


# def _array_to_node(input_heap: MaxHeap, index: int) -> TreeNode:
#     left = None
#     right = None
#     if input_heap.has_left(index):
#         left = _array_to_node(input_heap, input_heap.left_child(index))
#     if input_heap.has_right(index):
#         right = _array_to_node(input_heap, input_heap.right_child(index))
#     root = TreeNode(input_heap.array[index], left, right)
#     return root

# def _array_to_tree(input_heap: MaxHeap) -> Tree:
#     return Tree(_array_to_node(input_heap, 0))
# #
# def _pretty_tree_helper(root, curr_index=0):
#     if root is None:
#         return [], 0, 0, 0

#     line1 = []
#     line2 = []
#     node_repr = str(root.key)

#     new_root_width = gap_size = len(node_repr)

#     # Get the left and right sub-boxes, their widths, and root repr positions
#     l_box, l_box_width, l_root_start, l_root_end = _pretty_tree_helper(root.left, 2 * curr_index + 1)
#     r_box, r_box_width, r_root_start, r_root_end = _pretty_tree_helper(root.right, 2 * curr_index + 2)

#     # Draw the branch connecting the current root to the left sub-box
#     # Pad with whitespaces where necessary
#     if l_box_width > 0:
#         l_root = (l_root_start + l_root_end) // 2 + 1
#         line1.append(' ' * (l_root + 1))
#         line1.append('_' * (l_box_width - l_root))
#         line2.append(' ' * l_root + '/')
#         line2.append(' ' * (l_box_width - l_root))
#         new_root_start = l_box_width + 1
#         gap_size += 1
#     else:
#         new_root_start = 0

#     # Draw the representation of the current root
#     line1.append(node_repr)
#     line2.append(' ' * new_root_width)

#     # Draw the branch connecting the current root to the right sub-box
#     # Pad with whitespaces where necessary
#     if r_box_width > 0:
#         r_root = (r_root_start + r_root_end) // 2
#         line1.append('_' * r_root)
#         line1.append(' ' * (r_box_width - r_root + 1))
#         line2.append(' ' * r_root + '\\')
#         line2.append(' ' * (r_box_width - r_root))
#         gap_size += 1
#     new_root_end = new_root_start + new_root_width - 1

#     # Combine the left and right sub-boxes with the branches drawn above
#     gap = ' ' * gap_size
#     new_box = [''.join(line1), ''.join(line2)]
#     for i in range(max(len(l_box), len(r_box))):
#         l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
#         r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
#         new_box.append(l_line + gap + r_line)

#     # Return the new box, its width and its root positions
#     return new_box, len(new_box[0]), new_root_start, new_root_end

# def pretty_tree(tree):
#     lines = _pretty_tree_helper(tree.root, 0)[0]
#     return '\n' + '\n'.join((line.rstrip() for line in lines))

# # added 11/02/2024 - Alan M H Beem
# def pretty_tree_from_heap(input_heap: MaxHeap) -> None:
#     pretty_tree(_array_to_tree(input_heap))

