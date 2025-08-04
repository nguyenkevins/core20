class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        store = []

        def dfs(node):
            if node.left:
                dfs(node.left)
            store.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return store[k-1]

