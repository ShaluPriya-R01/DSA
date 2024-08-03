class Solution:
    def isPrime (self, N):
        if(N==1):
            return 0
        if (N<=3):
            return 1
        if (N%2==0):
            return 0
        for i in range(3, int(N**0.5)+1,2):
            if N%i==0:
                return 0
        return 1
            