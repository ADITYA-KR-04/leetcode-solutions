class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int
        :type initialExperience: int
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """
        A=sum(energy)
        B=sum(experience)
        ans=0
        if initialEnergy>A:
            if initialExperience>B:
                ans=0
            else:
                for i in range(len(energy)):
                    if experience[i]>=initialExperience:
                        ans+=(experience[i])-initialExperience+1
                        initialExperience+=2*(experience[i])-initialExperience+1
                    else:
                        initialExperiece=experience[i]
        else:
            ans+=A-initialEnergy+1
            if initialExperience>B:
                ans+=0
            else:
                for i in range(len(energy)):
                    if experience[i]>=initialExperience:
                        ans+=(experience[i])-initialExperience+1
                        initialExperience+=2*(experience[i])-initialExperience+1
                    else:
                        initialExperience+=experience[i]
        return ans