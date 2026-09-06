class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        last_seen = [-1] * 128
        
        max_length = 0
        left = 0
        
     
        for right, char in enumerate(s):
            char_code = ord(char)
        
            if last_seen[char_code] >= left:
                left = last_seen[char_code] + 1
                
            last_seen[char_code] = right
            
     
            window_size = right - left + 1
            if window_size > max_length:
                max_length = window_size
                
        return max_length
