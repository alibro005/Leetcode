class Solution:
    def maxFreqSum(self, s: str) -> int:
        if len(s) == 0:
            return 0

        freq = dict()

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        vowels = "aeiou"
        max_vowel = 0
        max_consonant = 0

        for key, value in freq.items():
            if key in vowels:
                if value > max_vowel:
                    max_vowel = value
            else:
                if value > max_consonant:
                    max_consonant = value

        return max_vowel + max_consonant
