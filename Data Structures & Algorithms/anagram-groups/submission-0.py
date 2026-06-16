class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        for sr in strs:
            key = tuple(sorted(sr))
            if key not in grp:
                grp[key] = []
            grp[key].append(sr)
        return list(grp.values()) 