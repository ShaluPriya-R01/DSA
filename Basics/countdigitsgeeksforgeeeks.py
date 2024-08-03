class Solution:
    def evenlyDivides (self, N):
        n=str(N)
        count=0
        for i in n:
            if int(i)!=0 and N%int(i)==0:
                count+=1
        return count