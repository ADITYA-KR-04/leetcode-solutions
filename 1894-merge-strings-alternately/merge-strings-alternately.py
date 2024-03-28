class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        s=""
        for i in range(min(len(word1),len(word2))):
            s+=word1[i]+word2[i]
        if len(word1)==len(word2):
            None
        elif len(word1)>len(word2):
            s+=word1[len(word2):]
        else:
            s+=word2[len(word1):]
        return s

        