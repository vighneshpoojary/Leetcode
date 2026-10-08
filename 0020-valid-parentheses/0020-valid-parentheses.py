class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                st.append(s[i])
            
            elif(len(st) == 0):
                return False
            elif st[-1] == '(' and s[i] == ')' or st[-1] == '{' and s[i] == '}' or st[-1] == '[' and s[i] == ']': 
                st.pop()
            else:
                return False
        return len(st) == 0

        