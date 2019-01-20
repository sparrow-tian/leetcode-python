class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        t=(['I',1],['V',5],['X',10],['L',50],['C',100],['D',500],['M',1000])
        d=dict(t)
        i=0
        sum=0
        l=list(s)
        while i < len(s):
            v=l[i]
            try:
                v1=l[i+1]
                if d[v] < d[v1]:
                    sum=sum+(d[v1]-d[v])
                    i+=2
                else:
                    sum+=d[v]
                    i+=1
            except:
                sum+=d[v]
                break
        return sum
