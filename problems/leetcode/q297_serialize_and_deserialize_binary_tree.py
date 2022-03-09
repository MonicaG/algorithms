from collections import deque
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.val} left: {self.left} right: {self.right}"


class Codec:

    TERMINUS = "n"
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
            else:
                result.append(self.TERMINUS)
                continue
            queue.append(node.left)
            queue.append(node.right)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) <= 0:
            return None
        nodes = data.split(",")
        root = TreeNode(nodes[0])
        queue = deque()
        queue.append(root)
        counter = 1
        while queue:
            node = queue.popleft()
            if nodes[counter] != self.TERMINUS:
                node_left = TreeNode(nodes[counter])
                node.left = node_left
                queue.append(node_left)
            counter += 1
            if nodes[counter] != self.TERMINUS:
                node_right = TreeNode(nodes[counter])
                node.right = node_right
                queue.append(node_right)
            counter += 1
        return root
