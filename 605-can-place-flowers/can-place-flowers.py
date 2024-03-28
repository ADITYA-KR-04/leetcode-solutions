class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        L=flowerbed
        spot=0
        if n==0:
            return True
        elif len(L)==1:
            if L[0]==0:
                return True
            else:
                return False
        else:
            for i in range(len(L)):
                if i!=0 and i!=(len(L)-1):
                    if L[i]==0 and L[i+1]==0 and L[i-1]==0:
                        spot+=1
                        L[i]=1
                elif i==0:
                    if L[i]==0 and L[i+1]==0:
                        spot+=1
                        L[i]=1
                else:
                    if L[i]==0 and L[i-1]==0:
                        spot+=1
                        L[i]=1
            if spot>=n:
                return True
            else:
                return False
