from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # The idea is to sort the array, drop all numbers greater than the target and think about what to do from there
        nums.sort(reverse=True)
        for idx in range(len(nums)):
            if nums[idx] > target:
                nums = nums[:idx]
                break
        minimal_sum = 0
        # Now we need to search for the highest number that can be added up to our target number
        for num in nums:
            if target - num in nums:
                minimal_sum = 2
            else:
                #TODO

        return minimal_sum





if __name__ == '__main__':
    sol = Solution()
    print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))