class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k==0:
            return 0
        elif set(nums)=={1} and k>1:
            a=len(nums)
            return (a*(a+1))//2 
        else:
            count=0
            i=0
            n=0
            m=1
            while(n!=len(nums)):
                if i==len(nums):
                    n+=1
                    i=n
                    m=1
                else:
                    m*=nums[i]
                    if m<k:
                        count+=1
                        i+=1
                    else:
                        n+=1
                        i=n
                        m=1
            return count


