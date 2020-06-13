class Solution {
public:
    /**
     * @param word input word to check if capitalization is correct
     * 
     * @return correct_capital
     * 
     * Given a string representing some word, you need to judge whether the 
     * usage of capitals in it is right or not.
     * 
     * Here the usage of capitals is defined to be correct if the following 
     * cases holds:
     *     1. All letters in this word are capitals, like "USA".
     *     2. All letters in this word are not capitals, like "leetcode".
     *     3  Only the first letter in this word is capital, like "Google".
     * Otherwise, we define that this word doesn't use capitals in a right way.
     *
     * This can be done in a single pass by counting how many capitals exist in
     * the input string. If there are no capitals, then condition 2 is 
     * satisfied. If there is one capital letter, and it occurs at the 
     * beginning of the string then condition 3 is satisfied. If the number of
     * capital letters is the same as the length of the string, then condition
     * 1 is satisfied.
     * 
     * Consider the example "USA". We start from the beginning of the string 
     * and count the number of capitals
     * 
     * "USA"
     *  ^
     * num_capitals = 1
     * 
     * "USA"
     *   ^
     * num_capitals = 2
     * 
     * "USA"
     *    ^
     * num_capitals = 3
     * 
     * Because the number of capitals equals the string length, condition 1
     * is satisfied and we return true.
     * 
     * The time complexity for this approach is O(n) where n is the length of
     * the string.
     * 
     * Examples
     * --------
     * Input : "USA"
     * Output : true
     * 
     * Input : "FlaG"
     * Output : false
     * 
     * Input : "NewYork"
     * Output : false
     * 
     * Input: "newyork"
     * Output : true
     */
    bool detectCapitalUse(string word) {
        if (word.length() < 2) {
            return true;
        }

        int32_t num_upper_case = 0;
        for (int i = 0; i < word.length(); ++i) {
            if (std::isupper(word[i])) {
                ++num_upper_case;
            }
        }
        
        // 3 bools are set, just for clarity
        // These are not necessary, and all of this can be done in a single
        // return statement.
        // determine if all the letters in the string are lower case
        bool all_lower = num_upper_case == 0;

        // determine if only the first letter in the string is upper case
        bool first_upper_only =  (num_upper_case == 1) && (std::isupper(word[0]));
        
        // determine if all characters in the string are upper case
        bool all_upper = num_upper_case == word.length();
        
        return all_lower || first_upper_only || all_upper;
    }
};