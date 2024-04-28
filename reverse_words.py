class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = s.split(' ')
        tmp = [i for i in tmp if i]
        return ' '.join(tmp[::-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseWords("a good   example"))
