from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        strs.sort(key=len)
        for idx, char in enumerate(strs[0]):
            i = 1
            while i < len(strs):
                if char == strs[i][idx]:
                   i += 1
                else:
                    return strs[0][:idx]
        return strs[0]



if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(["ab", "a"]))
