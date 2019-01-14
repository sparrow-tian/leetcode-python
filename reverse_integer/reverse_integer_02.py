import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=1 if x > 0 else -1
        boundary=math.pow(2,31)-1
        y=abs(x)
        listy=list(str(y))
        listy.reverse()
        result=int("".join(listy))
        return sign * result if result <= boundary else 0
