from heapq import heappop,heappush
class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        L=[]
        for i in range(len(profits)):
            L.append([capital[i],-profits[i]])
        prof=0
        L.sort()
        ops=0
        heap=[]
        i=0
        while(ops<k):
            while(i<len(L)):
                if w>=L[i][0]:
                    heappush(heap,L[i][1])
                    i+=1
                else:
                    break
            if heap and heap[0]<0:
                w-=heappop(heap)
                ops+=1
            else:
                break
        return w