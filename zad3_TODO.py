"""
Uzupełnij 2 funkcje poniżej oznaczone jako "TODO".
Nie modyfikuj kodu, który już istnieje.
Można tworzyć własne funkcje pomocnicze.
Po zaimplementowaniu rozwiązania komendy `pass` powinny być usunięte.
"""

from typing import List, Optional

class Solution(object):
    def req_count(self,root, integer):
        if(root):
            integer+=1
            buf1=self.req_count(root.left,integer)
            buf2=self.req_count(root.right,integer)
            if(buf1>buf2):
                integer=buf1
            else:
                integer=buf2
        return integer
    def get_height(self,root) :
        buf=self.req_count(root,0)
        return buf
    def maxDepth(self, root):
        return self.get_height(root)
    def isBalanced(self, root):
        if(not root):
            return True
        left=self.get_height(root.left)
        right=self.get_height(root.right)
        #print("a")
        buf=abs(left-right)
        #print(buf)
        if(buf>1):
            return False
        return self.isBalanced(root.left) and  self.isBalanced(root.right)
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


def get_height(root: Optional[Node]) -> int:
    buf=Solution()
    return buf.maxDepth(root)-1
def is_balanced(root: Optional[Node]) -> bool:
    b= Solution()
    return b.isBalanced(root)
# nie modyfikuj poniższego kodu
if __name__ == "__main__":
    node_values = input().strip().split(" ")
    root = create_binary_tree(node_values)
    height = get_height(root)
    if_balanced = int(is_balanced(root))
    print(height, if_balanced)
