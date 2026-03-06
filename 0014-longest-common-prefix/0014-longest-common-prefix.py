class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        f=strs[0]
        l=strs[-1]
        result=[]
        for i in range(len(f)):
            if(f[i]!=l[i]):
                break
            result.append(f[i])
        return "".join(result)