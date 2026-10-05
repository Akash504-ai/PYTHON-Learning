class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}

        for s in strs:
            sorted_s = sorted(s)
            key = ''.join(sorted_s)

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())