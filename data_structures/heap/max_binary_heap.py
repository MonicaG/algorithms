class MaxHeap:
    __NOT_FOUND__ = -99

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
        trickle_item_index = 0
        if len(self.__data) > 0:
            self.__data[0] = trickle_item
            # re-evaluate this. Maybe can do with iterating over array instead of doing the multiple checks
            while self.__has_larger_child(trickle_item_index):
                largest_child_index = self.__get_largest_child_index(trickle_item_index)
                self.__data[trickle_item_index], self.__data[largest_child_index] = self.__data[largest_child_index], self.__data[trickle_item_index]

        return removed_item

    def __has_larger_child(self, trickle_item_index):
        index = self.__get_largest_child_index(trickle_item_index)
        if index == MaxHeap.__NOT_FOUND__:
            return False
        else:
            return self.__data[trickle_item_index] < self.__data[index]

    def __get_largest_child_index(self, trickle_item_index):
        right_index = self.__right_child_index(trickle_item_index)
        left_index = self.__left_child_index(trickle_item_index)
        if right_index < len(self.__data):
            return right_index if self.__data[right_index] > self.__data[left_index] else left_index
        elif left_index < len(self.__data):
            return left_index
        else:
            return MaxHeap.__NOT_FOUND__

    def insert(self, value):
        self.__data.append(value)
        new_node_index = len(self.__data) - 1

        while new_node_index > 0 and self.__data[new_node_index] > self.__data[self.__parent_index(new_node_index)]:
            self.__data[new_node_index], self.__data[self.__parent_index(new_node_index)] = self.__data[self.__parent_index(new_node_index)], self.__data[new_node_index]
            new_node_index = self.__parent_index(new_node_index)

