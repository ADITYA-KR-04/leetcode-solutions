from collections import deque
class Solution(object):
    def orangesRotting(self, grid):

        t=0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    t+=1
        if t==0:return 0
        def adja(m,n):
            L=[]
            for i in range(m):
                L.append([[] for _ in range(n)])
            return L

        for i in range(t):
            adj=adja(m,n)
            for j in range(m):
                for k in range(n):
                    if grid[j][k]==2:
                        if j+1<m:adj[j][k].append((j+1,k))
                        if j-1>=0:adj[j][k].append((j-1,k))
                        if k+1<n:adj[j][k].append((j,k+1))
                        if k-1>=0:adj[j][k].append((j,k-1))
            
            for j in range(m):
                for k in range(n):
                    if grid[j][k]==2:
                        for neighbour in adj[j][k]:
                            if grid[neighbour[0]][neighbour[1]]!=0:grid[neighbour[0]][neighbour[1]]=2

            ans=True
            for j in range(m):
                for k in range(n):
                    if grid[j][k]==1:
                        ans=False
                        break
                if not ans:
                    break
            if ans:return i+1
        return -1