class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        
        n, m = len(text1), len(text2)

        # Create a DP table with (m+1) x (n+1) dimensions
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[j - 1] == text2[i - 1]:  # Match case
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:  # No match, take max of previous results
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[m][n]