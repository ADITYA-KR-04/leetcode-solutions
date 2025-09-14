from collections import defaultdict

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        n=len(arr)
        freq=defaultdict(int)
        carr=[]

        for i in range(n):
            freq[arr[i]]+=1
        
        for i in range(n):
            if freq[arr[i]]==1:
                carr.append(arr[i])

        if k>len(carr):
            return ""

        return carr[k-1]