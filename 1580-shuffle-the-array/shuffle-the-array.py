class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        L=[]
        for i in range(n):
            L.append(nums[i])
            L.append(nums[(n+i)])
        return L
        