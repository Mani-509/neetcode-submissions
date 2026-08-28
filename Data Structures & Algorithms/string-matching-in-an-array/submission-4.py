class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        for ch in words:
            for i in range(len(words)):
                if ch in words[i] and ch!=words[i]:
                    res.append(ch)
                    break
        return res