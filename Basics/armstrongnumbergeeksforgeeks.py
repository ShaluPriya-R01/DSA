
class Solution:
    def armstrongNumber (self, n):
        sum=0
        n_str=str(n)
        for digits in n_str:
            sum+= int(digits)**3
        if sum==n:
            return "true"
        return "false"