class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapdict={}
        for word in strs:
            sorted_word="".join(sorted(word))
            if sorted_word not in mapdict:
                mapdict[sorted_word]=[]
            mapdict[sorted_word].append(word)
        return list(mapdict.values())

    