class Solution:
    # @return a list of strings, [s1, s2]
    def dfs(self, num, string, res, length, digits):
        dict = {'1': [' '],
                '2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
        }

        if num == length:
            res.append(string)
            return

        for letter in dict[digits[num]]:
            self.dfs(num+1, string+letter, res, length, digits)

    def letterCombinations(self, digits):
        res = []
        length = len(digits)
        self.dfs(0, '', res, length, digits)
        return res

print Solution().letterCombinations('239')
