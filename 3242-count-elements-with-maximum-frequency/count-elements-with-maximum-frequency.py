class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        d=dict()
        for ls in nums:
            if ls not in d:
                d[ls]=1
            else:
                d[ls]+=1
        freq=0
        counts=0
        for x in d.values():
            if x>freq:
                freq=x
                counts=x
            elif x==freq:
                counts+=x
           
        return counts


        