from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode|None) -> TreeNode|None:
        """
                    4
            2                   7
           1  3                6  9
        
        Do a BFS or DFS, switch left subtree with right subtree, process next layer
        """
        if not root:
            return root

        que = Queue()
        que.put(root)

        while que.empty():
            item: TreeNode = que.get()
            
            
            left = item.left
            right = item.right
            item.left = right
            item.right = left
            if item.left:
                que.put(item.left)
            if item.right:
                que.put(item.right)

        return root