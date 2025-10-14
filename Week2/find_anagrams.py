# d https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

def findAnagrams(self, s: str, p: str) -> List[int]:

    ans = []
    for i in range(0, len(s)): 
        if isAnagram(s[i:i+len(p)],p):
            ans.append(i)
    return ans
    
def isAnagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2): return False
    count = {}
    for ch in s1:
        count[ch] = count.get(ch, 0) + 1

    for ch in s2:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False

    return True