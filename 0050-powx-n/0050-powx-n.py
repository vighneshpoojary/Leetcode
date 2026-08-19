class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans = 1
        if(x == 0 ):
            return 0.0
        if(n == 0 and x == 1):
            return 1.0
        if(x == -1 and n%2 == 0):
            return 1.0
        if(x == -1 and n%2 != 0 ):
            return -1.0

        if(n<0):
            x = 1/x
            n = abs(n)
        while(n>0):
            if n%2 == 1:
                ans *= x
            x *= x
            n = n//2
        return float(ans)
