class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        num_tmp = num
        while num_tmp > 0:
            if num_tmp - 1000 >= 0:
                res += 'M'
                num_tmp -= 1000
            elif num_tmp - 900 >= 0:
                res += 'CM'
                num_tmp -= 900
            elif num_tmp - 500 >= 0:
                res += 'D'
                num_tmp -= 500
            elif num_tmp - 400 >= 0:
                res += 'CD'
                num_tmp -= 400
            elif num_tmp - 100 >= 0:
                res += 'C'
                num_tmp -= 100
            elif num_tmp - 90 >= 0:
                res += 'XC'
                num_tmp -= 90
            elif num_tmp - 50 >= 0:
                res +='L'
                num_tmp -= 50
            elif num_tmp - 40 >= 0:
                res +='XL'
                num_tmp -= 40
            elif num_tmp - 10 >= 0:
                res += 'X'
                num_tmp -= 10
            elif num_tmp - 9 >= 0:
                res += 'IX'
                num_tmp -= 9
            elif num_tmp - 5 >= 0:
                res += 'V'
                num_tmp -= 5
            elif num_tmp - 4 >= 0:
                res += 'IV'
                num_tmp -= 4
            else:
                res += 'I'
                num_tmp -= 1

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.intToRoman(1994))
