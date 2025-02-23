from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1

        candies_l = [0] * len(ratings)
        candies_r = [0] * len(ratings)
        idx = 1
        for rating in ratings[1:]:
            if rating > ratings[idx-1]:
                candies_l[idx] = candies_l[idx-1] + 1
            idx += 1

        idx = len(ratings) -2
        # if ratings[-1] > ratings[-2]:
        #     candies_r[-1] += 1
        while idx >= 0:
            if ratings[idx] > ratings[idx+1]:
                candies_r[idx] = candies_r[idx+1] + 1
            idx -= 1
        res = [1] * len(ratings)
        for idx, val in enumerate(candies_l):
            res[idx] += max(val, candies_r[idx])
        # return sum(candies_l) + sum(candies_r) + len(ratings)
        return sum(res)
if __name__ == '__main__':
    sol = Solution()
    print(sol.candy([1,2,3,1,0]))
# [1,2,22,22,22,2,1]
# [1,2,3,1,1,1,1]
# [1,1,1,1,3,2,1]
# [1,2,3,1,3,2,1] = 13
