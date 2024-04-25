class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp={}
        m=len(text1)
        n=len(text2)
        def solve(text1,text2,m,n):
            if m==0 or n==0:
                return 0
            elif (m,n) in dp:
                return dp[(m,n)]
            else:
                if text1[m-1]==text2[n-1]:
                    c=1+solve(text1,text2,m-1,n-1)
                else:
                    c1=solve(text1,text2,m-1,n)
                    c2=solve(text1,text2,m,n-1)
                    c=max(c1,c2)
                dp[(m,n)]=c
                return c
        return solve(text1,text2,m,n)