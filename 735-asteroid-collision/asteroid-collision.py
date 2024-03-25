class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        i=0
        while(i<(len(asteroids)-1)):
            if (asteroids[i]>0 and asteroids[i+1]>0) or (asteroids[i]<0 and asteroids[i+1]<0) or (asteroids[i]<0 and asteroids[i+1]>0):
                i+=1
            else:
                if asteroids[i]==(-1)*asteroids[i+1]:
                    asteroids.pop(i+1)
                    asteroids.pop(i)
                elif abs(asteroids[i])>abs(asteroids[i+1]):
                    asteroids.pop(i+1)
                else:
                    asteroids.pop(i)
                if i>0:
                    i-=1
                else:
                    continue
        return asteroids