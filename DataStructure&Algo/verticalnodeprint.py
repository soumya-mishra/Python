import pdb
# Data Structure to store a binary tree node
class Node:
    def __init__(self, key, left=None, right=None):

        self.key = key
        self.left = left
        self.right = right


# Recursive function to do a pre-order traversal of the tree and fill dict
# Here node has 'dist' horizontal distance from the root of the tree
def printVertical(node, dist, dict):

    # base case: empty tree
    if node is None:
        return

    # insert nodes present at current horizontal distance into the dict
    dict.setdefault(dist, []).append(node.key)
    
    # {0: [1, 5], -1: [2], 1: [3]}
#     pdb.set_trace()
    # recur for left subtree by decreasing horizontal distance by 1
    printVertical(node.left, dist - 1, dict)

    # recur for right subtree by increasing horizontal distance by 1
    printVertical(node.right, dist + 1, dict)


# Function to perform vertical traversal of a given binary tree
def printVerticalTree(root):

    # create an empty TreeDictionary where
    # key -> relative horizontal distance of the node from root node and
    # value -> nodes present at same horizontal distance
    dict = {}

    # do pre-order traversal of the tree and fill the dict
    printVertical(root, 0, dict)
#     pdb.set_trace()
    # traverse the dictionary and print vertical nodes
    for value in dict.values():
        print(value)


if __name__ == '__main__':

    """ Construct below tree
              1
            /   \
           /     \
          2       3
                /   \
               /     \
              5       6
            /   \
           /     \
          7       8
                /   \
               /     \
              9      10
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    root.right.left.right.left = Node(9)
    root.right.left.right.right = Node(10)

    printVerticalTree(root)
