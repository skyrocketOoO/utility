import queue

class Solution:
    def minimumMoves(self, grid) -> int:
        self.ans = 0
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    self.backtrack(i, j, grid, 0, 0)
        return self.ans
    def backtrack(self, i, j, grid, step, ans):
        visited = set()
        self.bfs(i, j, visited, step, ans)


    def bfs(self, i, j, visited, step, ans):
        if (i, j) in visited:
            return
        q = queue.Queue()
        q.put((i, j))
        step = 0
        find = False
        while not q.empty() and find is False:
            for _ in range(q.qsize()):
                a, b = q.get()
                if (a, b) in visited:
                    continue
                if grid[a][b] > 1:
                    grid[i][j] = 1
                    grid[a][b] -= 1
                    ans += step
                    find = True
                    break
                visited.add((a, b))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x = dx + a
                    y = dy + b
                    if x < 0 or x > 2 or y < 0 or y > 2:
                        continue
                    q.put((x, y))
            step += 1

        


grid = [[3,2,0],[0,1,0],[0,3,0]]
s=  Solution()
print(s.minimumMoves(grid))
