from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(grid, row, col):
            grid[row][col] = '0'
            queue = deque()
            queue.append((row, col))
            while len(queue):
                i, j = queue.popleft()
                offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
                for offset in offsets:
                    offseti, offsetj = offset

                    if (0 <= i + offseti < len(grid) and
                        0 <= j + offsetj < len(grid[0]) and
                            grid[i + offseti][j + offsetj] == '1'):
                        # mark as visited and add to queue
                        queue.append((i + offseti, j + offsetj))
                        grid[i + offseti][j + offsetj] = '0'

        # iterate over each element and run a bfs
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    bfs(grid, i, j)
        return count
