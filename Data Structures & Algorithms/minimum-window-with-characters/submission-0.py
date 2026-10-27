from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        t_count = Counter(t)
        window = {}
        
        required = len(t_count)
        formed = 0
        
        left = 0
        min_len = float('inf')
        ans_left = 0
        
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            if char in t_count and window[char] == t_count[char]:
                formed += 1
                
            while left <= right and formed == required:
                char_left = s[left]
                
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans_left = left
                    
                window[char_left] -= 1
                if char_left in t_count and window[char_left] < t_count[char_left]:
                    formed -= 1
                    
                left += 1
                
        return "" if min_len == float('inf') else s[ans_left:ans_left + min_len]