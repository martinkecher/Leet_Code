
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Remove all non-alphanumeric chars
        # 2. Change all chars to lower case
        # 3. Check if the string left is a palindrome
        # 4. Return True/ False
        st = ''
        for ch in s:
            if ch.isalpha() or ch.isnumeric():
                st = st + ch
        st = st.lower()

        for idx in range(int(len(st)/2)):
            if st[idx] != st[len(st) - 1 - idx]:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama")) # True
