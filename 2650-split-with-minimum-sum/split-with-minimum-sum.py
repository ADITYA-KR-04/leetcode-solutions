class Solution:
    def splitNum(self, num: int) -> int:
        
        a=[]
        while num!=0:

            a.append(num%10)
            num//=10

        a.sort()
        p1,p2=0,0

        for i in range(len(a)):

            if i%2:
                p1=10*p1+a[i]
            else:
                p2=10*p2+a[i]

        return p1+p2