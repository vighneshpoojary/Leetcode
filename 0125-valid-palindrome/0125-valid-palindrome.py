class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        value = re.sub('[^a-zA-Z0-9]','',s).lower()
        
        i = 0 
        j = len(value)-1
        while i<j:
            if value[i] == value[j]:
                i += 1
                j -= 1
            else:
                return False

        return True

        