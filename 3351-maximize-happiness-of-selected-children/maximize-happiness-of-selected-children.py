class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort()
        n=len(happiness)
        L=happiness[(n-k):n]
        sum=0
        for i in range(k):
            if (L[k-i-1]-i)>0:
                sum+=(L[k-i-1]-i)
        return sum

