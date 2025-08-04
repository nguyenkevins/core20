class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        y_length = len(board)
        x_length = len(board[0]) 
        store = [[False for _ in range(x_length)] for _ in range(y_length)]

        def dfs(x, y, i):
            if i == len(word):
                return True
            if y == y_length or x == x_length or y == -1 or x == -1 or store[y][x] or board[y][x] != word[i]:
                return False
            
            store[y][x] = True
            result = dfs(x + 1, y, i + 1) or dfs(x - 1, y, i + 1) or dfs(x, y + 1, i + 1) or dfs(x, y - 1, i + 1)
            store[y][x] = False
            return result

        for y in range(0, y_length):
            for x in range(0, x_length):
                if dfs(x, y, 0) == True:
                    return True
        return False

