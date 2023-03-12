class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        row, col = len(s) + 1, len(p) +  1
        dp = [[False for j in range(col)] for i in range(row)]


        # initilize the dp
        dp[0][0] = True
        for j in range(1, col):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]
        
        for i in range(1, row):
            for j in range(1, col):
                string, pattern = s[i - 1], p[j - 1]
                
                if pattern == '*':
                    dp[i][j] = dp[i - 1][j - 1] or dp[i -1][j] or dp[i][j - 1]
                elif pattern == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = (string == pattern) and dp[i - 1][j - 1]

        return dp[-1][-1]
        