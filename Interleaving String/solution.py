class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        self.memo = defaultdict(lambda:-1)
        def check(s1,s2,s3,i,j,k,n1,n2,n3):
            if self.memo[(s1,s2,s3,i,j,k,n1,n2,n3)] != -1:
                return self.memo[(s1,s2,s3,i,j,k,n1,n2,n3)]
            if n1 + n2 != n3:
                self.memo[(s1,s2,s3,i,j,k,n1,n2,n3)] = False
                return False
            if i >= n1 and j >= n2 and k >= n3:
                self.memo[(s1,s2,s3,i,j,k,n1,n2,n3)] = True
                return True
            if i >= n1:
                self.memo[(s1,s2,s3,i,j,k,n1,n2,n3)] = s2[j:] == s3[k:]
                return self.memo[(s1,s2,s3,i,j,k,n1,n2,n3)]
            if j >= n2:
                self.memo[(s1,s2,s3,i,j,k,n1,n2,n3)] = s1[i:] == s3[k:]
                return self.memo[(s1,s2,s3,i,j,k,n1,n2,n3)]
            if s1[i] == s3[k] and s2[j] == s3[k]:
                self.memo[(s1,s2,s3,i,j,k,n1,n2,n3)] = check(s1,s2,s3,i + 1,j,k + 1,n1,n2,n3) or check(s1,s2,s3,i,j + 1,k + 1,n1,n2,n3)
                return self.memo[(s1,s2,s3,i,j,k,n1,n2,n3)]
            elif s1[i] == s3[k]:
                self.memo[(s1,s2,s3,i,j,k,n1,n2,n3)] = check(s1,s2,s3,i + 1,j,k + 1,n1,n2,n3)
                return self.memo[(s1,s2,s3,i,j,k,n1,n2,n3)]
            elif s2[j] == s3[k]:
                self.memo[(s1,s2,s3,i,j,k,n1,n2,n3)] = check(s1,s2,s3,i,j + 1,k + 1,n1,n2,n3)
                return self.memo[(s1,s2,s3,i,j,k,n1,n2,n3)]
            else:
                self.memo[(s1,s2,s3,i,j,k,n1,n2,n3)] = False
                return False
        return check(s1,s2,s3,0,0,0,len(s1),len(s2),len(s3))
        
                
            
