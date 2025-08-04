# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        store = []
        queueList = collections.deque()
        queueList.append(root)
        
        while queueList:
            tempStore = []
            for i in range(len(queueList)):
                pop = queueList.popleft()
                tempStore.append(pop.val)
                if pop.left:
                    queueList.append(pop.left)
                if pop.right:
                    queueList.append(pop.right)
            store.append(tempStore)
        return store
                
