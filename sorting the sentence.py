class Solution:
    def sortSentence(self, s: str) -> str:
        a = list(s.split(' '))
        new = []
        for i in range(1,(len(a)+1)):
            for j in range (len(a)):
                if i == int(a[j][-1]):
                    c = a[j]
                    l = c[:-1]
                    new.append(l)
                    break
        return " ".join(new)
