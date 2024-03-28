class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        k=max(candies)
        L=[]
        for i in range(len(candies)):
            if candies[i] + extraCandies < k:
                L.append(False)
            else:
                L.append(True)
        return L
        