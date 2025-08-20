class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = {}
        l, result = 0, 0
        for r in range(0, len(s)):
            store[s[r]] = store.get(s[r], 0) + 1
            while r - l - max(store.values()) + 1 > k:
                store[s[l]] -= 1
                l += 1
            result = max(result, r-l+1)
        return result
