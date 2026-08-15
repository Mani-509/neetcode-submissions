from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Initialize an array of 26 zeros
            count = [0] * 26 
            
            for char in s:
                # Increment the count for the specific character
                count[ord(char) - ord('a')] += 1
                
            # Tuples are immutable and hashable, so they can be dictionary keys
            anagram_map[tuple(count)].append(s)
            
        return list(anagram_map.values())