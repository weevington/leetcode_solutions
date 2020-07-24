class Solution {
public:
    bool is_palindrome(const std::string& s) {
        size_t lo = 0;
        size_t hi = s.length() - 1;
        
        while (lo < hi) {
            if (s[lo] != s[hi]) {
                return false;
            }
            ++lo;
            --hi;
        }
        return true;
    }
    
    /**
     * @param s
     * 
     * Given a non-empty string s, returns whether the given string can be 
     * made into a palindrome with the removal of up to 1 character.
     *
     * Conider the example "aba". This string is a palindrome, so there is
     * nothing to remove.
     *
     * Now consider the example "racebcar". Normally, "racecar" is a classic 
     * example of a palindrome, bue the presence of the "b" in the string 
     * prevents it from being a palindrome. However, if we remove the single
     * character 'b', then we recover "racecar".
     *
     * We can use two pointers, one from the end of the string, and one from
     * the start of the string. 
     *
     *                                  "racebcar"
     *                                   ^      ^
     *                                  lo      hi
     *
     * If s[lo] is equal to s[hi], then we proceed to increment lo and
     * decrement hi.
     *                                  "racebcar"
     *                                    ^    ^
     *                                   lo    hi
     *
     *
     *                                  "racebcar"
     *                                     ^  ^
     *                                    lo  hi
     *
     *
     *                                  "racebcar"
     *                                      ^^
     *                                     lohi
     *
     * Here, we have the condition s[lo] is not equal to s[hi]. We can remove
     * up to one character, but we don't know if the offending character is 
     * s[lo] or s[hi]. We can rebuild the string, excluding s[lo], and we can
     * rebuild a different string, excluding s[hi]. If we exclude s[lo], we
     * obtain "racbcar", which is a palindrome. If we were to remove s[hi], we
     * obtain "racecar", which is also a palindrome. In this particular 
     * example, it turns out that we can achieve a palindrome by removing 
     * either s[lo] or s[hi], but that is not the general case. Therefore, in
     * general, if s[lo] is not equal to s[hi], we build the two different 
     * substrings strings out of the original string, one without s[lo] and 
     * one without s[hi]. We test each of these new substrings to see if 
     * either one is a palindrome, in which case we return True, otherwise
     * we return False. 
     */
    bool validPalindrome(const std::string& s) {
        const size_t s_len = s.length();
        if (!s_len) {
            return true;
        }

        size_t lo = 0;
        size_t hi = s_len - 1;
        while (lo < hi) {
             if (s[lo] != s[hi]) {
                std::string test_one = s.substr(0, lo) + s.substr(lo + 1);
                std::string test_two = s.substr(0, hi) + s.substr(hi + 1);
                
                return is_palindrome(test_one) || is_palindrome(test_two);
            }
            ++lo;
            --hi;
        }
        
        return true;
    }
};