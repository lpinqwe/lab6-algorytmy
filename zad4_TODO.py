"""
Uzupełnij 1 funkcje poniżej oznaczoną jako "TODO". 
Nie modyfikuj kodu, który już istnieje.
Można tworzyć własne funkcje pomocnicze.
Po zaimplementowaniu rozwiązania komendy `pass` powinny być usunięte.
"""

from typing import List, Optional
class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(node_values: List[str]):
    if (
            not node_values
            or len(node_values) == 0
            or node_values[0].strip() == ""
            or node_values[0] == "null"
    ):
        return None
    root = Node(int(node_values[0]))
    queue = [(root, 0)]
    while queue:
        current_node, idx = queue.pop()
        left_idx = idx * 2 + 1
        right_idx = idx * 2 + 2
        if left_idx < len(node_values):  # left child
            value = node_values[left_idx]
            if value != "null":
                current_node.left = Node(int(value))
                if left_idx <= len(node_values) // 2:  # is not a leaf
                    queue.append((current_node.left, left_idx))

        if right_idx < len(node_values):  # right child
            value = node_values[right_idx]
            if value != "null":
                current_node.right = Node(int(value))
                if right_idx <= len(node_values) // 2:  # is not a leaf
                    queue.append((current_node.right, right_idx))

    return root


def get_left_subtree(root: Optional[Node]):
    if root:
        return root.left
    return None


def get_right_subtree(root: Optional[Node]):
    if root:
        return root.right
    return None


def inorder( root, output):
    if root is None:
        return
    inorder(root.left, output)
    output.append(root.val)
    inorder(root.right, output)

def is_valid_BST(root: Optional[Node]) -> bool:
    output = []
    inorder(root, output)
    print(output)
    for i in range(1, len(output)):
        if output[i - 1] >= output[i]:
            return False

    return True


# nie modyfikuj poniższego kodu
if __name__ == "__main__":
    node_values = input().strip().split(" ")
    root = create_binary_tree(node_values)
    subRoot1 = get_left_subtree(root)
    subRoot2 = get_right_subtree(root)
    print(is_valid_BST(root), is_valid_BST(subRoot1), is_valid_BST(subRoot2))
