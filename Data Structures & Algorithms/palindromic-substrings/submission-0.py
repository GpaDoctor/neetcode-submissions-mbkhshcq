class Solution:

  def countSubstrings(self, s: str) -> int:
    n, res = len(s), 0
    # dp[i][j] will be True if the substring s[i...j] is a palindrome
    dp = [[False] * n for _ in range(n)]

    # Iterate backwards from the last character to the first character
    # This ensures that dp[i + 1][j - 1] is already computed when evaluating dp[i][j]
    for i in range(n - 1, -1, -1):
      # Iterate forward from the current start index 'i' to the end of the string
      for j in range(i, n):
        # A substring s[i...j] is a palindrome if:
        # 1. The outer characters match (s[i] == s[j])
        # 2. Either the length is 3 or less (j - i <= 2),
        #    meaning it's a 1-character, 2-character, or 3-character palindrome,
        #    OR the inner substring (s[i+1...j-1]) is already known to be a palindrome (dp[i+1][j-1] is True).
        if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
          dp[i][j] = True
          res += 1  # Increment the total palindrome count

    return res