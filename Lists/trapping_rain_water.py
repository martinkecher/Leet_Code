from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left_idx: int = 0
        right_idx: int = 1 if len(height) > 1 else 0
        if right_idx == 0: return 0
        rain_count = 0

        while right_idx < len(height):
            if height[right_idx] < height[left_idx]:
                right_idx += 1
            else:
                for i in range(left_idx + 1, right_idx):
                    rain_count += abs(height[left_idx] - height[i])
                left_idx = right_idx
                right_idx += 1

        max_idx = left_idx
        right_idx = len(height) - 1
        left_idx = right_idx - 1
        if left_idx == max_idx: return rain_count

        while left_idx >= max_idx:
            if height[left_idx] < height[right_idx]:
                left_idx -= 1
            else:
                for i in range(right_idx - 1, left_idx, -1):
                    rain_count += height[right_idx] - height[i]
                right_idx = left_idx
                left_idx -= 1
        return rain_count


if __name__ == '__main__':
    sol = Solution()
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
