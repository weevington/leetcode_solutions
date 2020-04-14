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

        This method uses a dictionary where the sorted words are the keys.
        Anagrams will have the same number of letter counts, so two anagrams
        should give the same result when sorted. Associate an array with each
        sorted key. Loop over each word; if the sorted word exists in the 
        dictionary, then append to the array associated with the given key,
        else, create a new key-value pair with. Return the values of the
        dictionary as a list of lists.

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
        ana_dict = {}
        for i, wd in enumerate(strs): #wd is word
            wd_sorted = "".join(sorted(wd))
            if not wd_sorted in ana_dict.keys():
                ana_dict[wd_sorted] = [wd]
            else:
                ana_dict[wd_sorted].append(wd)
        
        return ana_dict.values()