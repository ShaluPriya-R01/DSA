class Solution:
    def isPerfectNumber(self, N):
        sum=1
        i=2
        while i*i<=N:
            if N%i==0:
                sum=sum+i+N//i
            i=i+1
        return(1 if sum==N and N!=1 else 0)