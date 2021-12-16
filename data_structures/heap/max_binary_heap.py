class MaxHeap:

    def __init__(self):
        self.__data = []

    def root_node(self):
        return self.__data[0]

    def last_node(self):
        return self.__data[-1]

    def __left_child_index(self, index: int):
        return (index * 2) + 1

    def __right_child_index(self, index: int):
        return (index * 2) + 2

    def __parent_index(self, index):
        return (index - 1) // 2

    def get_list(self):
        return self.__data[0:]

    def pop(self):
        removed_item = self.__data[0]
        trickle_item = self.__data.pop()
        if self.__data:
            self.__data[0] = trickle_item
            self.__trickle(0)
        return removed_item

    def __trickle(self, position):
        end_position = len(self.__data)
        did_trickle = True
        while position < end_position and did_trickle:
            left_child_index = self.__left_child_index(position)
            right_child_index = self.__right_child_index(position)
            index = end_position
            if right_child_index < end_position:
                index = right_child_index if self.__data[right_child_index] > self.__data[left_child_index] \
                    else left_child_index
            elif left_child_index < end_position:
                index = left_child_index
            if index < end_position and self.__data[position] < self.__data[index]:
                self.__data[position], self.__data[index] = self.__data[index], self.__data[position]
            else:
                did_trickle = False
            position = index

    def insert(self, value):
        self.__data.append(value)
        new_node_index = len(self.__data) - 1

        while new_node_index > 0 and self.__data[new_node_index] > self.__data[self.__parent_index(new_node_index)]:
            self.__data[new_node_index], self.__data[self.__parent_index(new_node_index)] = self.__data[self.__parent_index(new_node_index)], self.__data[new_node_index]
            new_node_index = self.__parent_index(new_node_index)

