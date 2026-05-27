class TrieNode:
    def __init__(self):
        # A dictionary to store child nodes where the key is the character 
        # and the value is the corresponding TrieNode.
        self.children = {}
        
        # A boolean flag to indicate if this node represents the end of a complete word.
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        # Initialize the Trie with a root node that contains no character.
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start the traversal from the root node.
        cur = self.root
        
        # Iterate through each character in the given word.
        for c in word:
            # If the character doesn't exist as a child, create a new TrieNode for it.
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move the pointer to the child node corresponding to the character.
            cur = cur.children[c]
            
        # After placing all characters, mark the final node's endOfWord as True.
        cur.endOfWord = True


    def search(self, word: str) -> bool:
            # Start the traversal from the root node.
            cur = self.root
            
            # Iterate through each character in the search word.
            for c in word:
                # If a character is missing, the word does not exist in the Trie.
                if c not in cur.children:
                    return False
                # Move to the next node in the path.
                cur = cur.children[c]
                
            # Return True only if we successfully matched all characters 
            # AND the current node represents the end of a complete word.
            return cur.endOfWord   

    def startsWith(self, prefix: str) -> bool:
            # Start the traversal from the root node.
            cur = self.root
            
            # Iterate through each character in the prefix.
            for c in prefix:
                # If any character in the prefix is missing, no word starts with it.
                if c not in cur.children:
                    return False
                # Move to the next node in the path.
                cur = cur.children[c]
                
            # If we successfully traversed the whole prefix, then at least one 
            # word shares this prefix. We don't care if it's a full word or not.
            return True
        
        