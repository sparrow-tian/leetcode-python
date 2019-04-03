class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) ==0:
            return 0
        for k,v in enumerate(haystack):
            l=0
            if v==needle[l] and len(haystack)-k >= len(needle):
                while(l < len(needle)):              
                    if haystack[k+l]==needle[l]:
                        l+=1
                    else:
                        break
  
                if l==len(needle):
                    return k
        return -1
