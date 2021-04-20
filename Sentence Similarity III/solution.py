class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        s1 = sentence1.split()
        s2 = sentence2.split()
        l1 = len(s1)
        l2 = len(s2)
        if l1 < l2:
            s1,s2 = s2,s1
            l1,l2 = l2,l2
        while s1 and s2 and s1[0] == s2[0]:
            s1.pop(0)
            s2.pop(0)
        
        while s1 and s2 and s1[-1] == s2[-1]:
            s1.pop()
            s2.pop()
        
        return len(s2) == 0
