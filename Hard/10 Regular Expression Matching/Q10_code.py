class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # let the dp: m x n matrix m : length of s and n: is the length of p 
        m, n = len(s) + 1, len(p) + 1   # extra 1 for empty space at the begining 
        dp = [[ False for x in range(n) ] for y in range(m)] 

        # empty is always equal to empty
        dp[0][0] = True
        for j in range(1, n):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m):
            for j in range(1, n):
                string, pattern = s[i - 1], p[j - 1]

                if pattern == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern != '*':
                    dp[i][j] = dp[i - 1][j - 1] and ( string == pattern )
                elif pattern == '*':
                    if p[j - 2] != '.':
                        dp[i][j] = dp[i][j - 2] or ( dp[i -1][j] and (string == p[j - 2]) )
                    else:
                        dp[i][j] = dp[i][j - 2] or dp[i -1][j]
        # print(dp)
        return dp[m - 1][n - 1]

