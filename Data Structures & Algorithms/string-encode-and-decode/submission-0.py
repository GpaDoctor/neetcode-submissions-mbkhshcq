from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Handle the edge case of an empty input list
        if not strs:
            return ""
        
        sizes, res = [], []
        
        # Step 1: Collect the length of each individual string
        for s in strs:
            sizes.append(len(s))
        
        # Step 2: Build the metadata header (e.g., "4,5,6,")
        for sz in sizes:
            res.append(str(sz))
            res.append(',')
            
        # Step 3: Place a marker '#' to separate the metadata header from the actual content
        res.append('#')
        
        # Step 4: Append all the original strings right after the '#' marker
        res.extend(strs)
        
        # Combine everything into a single encoded string
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        # Handle the edge case of an empty encoded string
        if not s:
            return []
            
        sizes, res, i = [], [], 0
        
        # Step 1: Parse the metadata header until we hit the '#' marker
        while s[i] != '#':
            j = i
            # Find the end of the current length integer (marked by a comma)
            while s[j] != ',':
                j += 1
            # Extract the integer size and add it to our sizes list
            sizes.append(int(s[i:j]))
            # Move the pointer past the comma to start reading the next size
            i = j + 1
            
        # Step 2: Skip past the '#' marker to position our pointer at the start of the text content
        i += 1
        
        # Step 3: Use the parsed sizes to slice out each original string sequentially
        for sz in sizes:
            res.append(s[i:i + sz])
            # Advance the pointer past the string we just extracted
            i += sz
            
        return res