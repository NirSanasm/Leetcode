class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anagram_list = defaultdict(list)


        for str in strs:

            sorted_val = ''.join(sorted(str))

            anagram_list[sorted_val].append(str)

        return list(anagram_list.values())
        