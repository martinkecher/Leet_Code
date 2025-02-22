from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        if len(height) < 2: return 0
        left_idx: int = 0
        right_idx: int = len(height) - 1

        while right_idx > left_idx:
            area = min(height[right_idx], height[left_idx]) * (right_idx - left_idx)
            max_area = area if max_area < area else max_area
            if height[right_idx] < height[left_idx]:
                right_idx -= 1
            else:
                left_idx += 1

        return max_area

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))