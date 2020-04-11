class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings, groups anagrams together. Grouped anagrams
        not necessarily sorted in lexicographic order.

        Parameters
        ----------
        strs: List[str]
            List of words with potential anagrams.

        Returns
        -------
        anagrams : List[List[str]]
            Grouped anagrams.

        Examples
        --------
        Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
        Output: [["ate","eat","tea"], ["nat","tan"], ["bat"]]
        """
        seen_wds = {}
        wd_index = 0

        anagrams = []
        for i in range(len(strs)):
            q = "".join(sorted(strs[i]))
            if seen_wds.get(q) is None:
                seen_wds[q] = wd_index
                anagrams.append([strs[i]])
                wd_index += 1
            else:
                j = seen_wds[q]
                anagrams[j].append(strs[i])

        return anagrams


# a tighter/neater solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings, groups anagrams together. Grouped anagrams
        not necessarily sorted in lexicographic order.

        Parameters
        ----------
        strs: List[str]
            List of words with potential anagrams

        Returns
        -------
        anagrams : List[List[str]]
            Grouped anagrams

        Examples
        --------
        Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
        Output: [["ate","eat","tea"], ["nat","tan"], ["bat"]]
        """
        d = {}
        
        for words in strs:
            sorted_word  = "".join(sorted(words))

            if sorted_word not in d:
                d[sorted_word]= [words]
            else:
                d[sorted_word].append(words)
                       
        return d.values()