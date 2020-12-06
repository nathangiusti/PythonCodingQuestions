
class Node:
    def __init__(self, value=0):
        self.value = 0
        self.left = None
        self.right = None


def make_tree(arr):
    node = Node()
    if len(arr) < 2:
        node.value = arr[0]
        if len(arr) > 1:
            node.left = Node(arr[1])
        return node
    median = round(len(arr)/2) - 1
    node.value = arr[median]
    node.left = make_tree(arr[:median])
    node.right = make_tree(arr[median+1:])
    return node


def search_tree(tree, val):
    if tree is None:
        return False
    if val == tree.value:
        return True
    elif val > tree.value:
        return search_tree(tree.right, val)
    else:
        return search_tree(tree.left, val)


tree = make_tree([1, 2, 3, 5, 6, 8, 9, 10, 12])

print(search_tree(tree, 7))
print(search_tree(tree, 15))
print(search_tree(tree, -1))
print(search_tree(tree, 1))
