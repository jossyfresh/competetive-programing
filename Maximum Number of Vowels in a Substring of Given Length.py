class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        count = 0
        vowel = "aeiou"
        maxi = 0
        for i in range(k):
            if s[i] in vowel:
                count+=1
        maxi = count
        for j in range (k,len(s)):
            if s[j] in vowel:
                count+=1
            if s[l] in vowel:
                count-=1
            l+=1
            maxi = max(maxi,count)
        return maxi 
