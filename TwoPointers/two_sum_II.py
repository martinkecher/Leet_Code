from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers[0] >= 0:
            for idx, num in enumerate(numbers):
                if num > target:
                    numbers = numbers[: idx]
        if target >= 0:
            idx2 = len(numbers)
            for num2 in numbers[ : : -1]:
                idx2 -= 1
                for num1 in numbers[idx2-1: :-1]:
                    idx1 = numbers.index(num1)
                    if num1 + num2 == target:
                        return [1+idx1, 1+idx2]
        else:
            for idx1, num1 in enumerate(numbers[: -1]):
                for idx2, num2 in enumerate(numbers[idx1+1 :]):
                    if num1 + num2 == target:
                        return [1+ idx1, 2+ idx1+idx2]
        return [-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([0,0,3,4], 0))
