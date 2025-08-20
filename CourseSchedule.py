class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Store visited (variable)
        visited = set()

        # Build graph
        graph = {i: [] for i in range(numCourses)}
        for u,v in prerequisites:
            graph[u].append(v)

        # Define DFS
        def dfs(c):
            if c in visited:
                return False
            if c == []:
                return True
            visited.add(c)
            for i in graph[c]:
                if not dfs(i):
                    return False
            visited.remove(c)
            return True

        # For-Loop to run DFS and test every courses
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
