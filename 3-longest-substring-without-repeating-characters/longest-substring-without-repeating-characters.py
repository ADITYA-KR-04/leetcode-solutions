from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        index=defaultdict(lambda:-1)
        if n==0:
            return 0
        j=0
        index[s[0]]=0
        ans=1

        for i in range(1,n):
            j=max(j,index[s[i]]+1)
            ans=max(ans,i-j+1)
            index[s[i]]=i

        return ans