class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n=len(gas)
        unvis=[0]*n
        start=0
        idx=0
        i=0

        while True:
            unvis[i]=1
            if cost[i]<=gas[i]+idx:
                idx+=gas[i]-cost[i]
                i=(i+1)%n
                if start==i:
                    return start
            else:
                i=(i+1)%n
                start=i%n
                idx=0
                if unvis[i]:
                    return -1