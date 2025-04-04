from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        deq = deque()
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                # put all 0s in the queue
                if mat[i][j] == 0:
                    deq.append((i, j, 0))
                # else set -1
                else:
                    mat[i][j] = -1

        while deq:
            i, j, distance = deq.popleft()

            # traverse all directions
            for direction_i, direction_j in direction:
                new_i = i + direction_i
                new_j = j + direction_j
                if new_i < 0:
                    new_i = 0
                elif new_i >= m:
                    new_i = m - 1
                if new_j < 0:
                    new_j = 0
                elif new_j >= n:
                    new_j = n - 1

                if mat[new_i][new_j] == -1:
                    mat[new_i][new_j] = distance + 1
                    deq.append((new_i, new_j, distance + 1))

        return mat