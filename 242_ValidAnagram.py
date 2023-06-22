class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if set(s) == set(t) and len(s) == len(t):
        #     return True
        # return False
        
        list_s = list(s)
        list_s.sort()
        list_t = list(t)
        list_t.sort()
        
        if list_s == list_t:
            return True
        return False