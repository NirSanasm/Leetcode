class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_so_far = 0
    
        initial = 0
        seen = {}
        for i in range(len(s)):

            if s[i] not in seen:
                max_so_far = max(max_so_far , i - initial + 1)
            else:
                if seen[s[i]] < initial:
                    max_so_far = max(max_so_far, i - initial + 1)

                else:
                    initial = seen[s[i]] + 1
                    
            
            seen[s[i]] = i     

        return max_so_far
            



        