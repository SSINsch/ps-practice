from typing import List
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        list_queue = deque([(sr, sc)])
        origin_color = image[sr][sc]

        if origin_color == color:
            return image

        while list_queue:
            i_sr, j_sc = list_queue.popleft()
            image[i_sr][j_sc] = color

            # will check left, right, up, down
            for i_r, i_c in [(i_sr-1, j_sc), (i_sr+1, j_sc), (i_sr, j_sc-1), (i_sr, j_sc+1)]:
                # need to check whether (x,y) is valid
                if 0 <= i_r < len(image) and 0 <= i_c < len(image[0]):
                    # check if it shares same color
                    if image[i_r][i_c] == origin_color:
                        list_queue.append((i_r, i_c))
                        image[i_r][i_c] = color

        return image


s = Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
print(s.floodFill([[0,0,0],[0,0,0]], 0, 0, 0))
