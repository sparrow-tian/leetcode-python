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
        result = 0
        while y:
            result=result * 10 + y % 10
            y=y // 10
        return sign * result if result < boundary else 0
