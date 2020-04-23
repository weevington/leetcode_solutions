class Solution {
public:
    /*
     * @brief helper function for rec 
     * 
     * @param s input vector of characters
     * @param pos current position/index used in recursion
     */
    void reverse_string_recursive(std::vector<char> &s, int32_t pos)
    {
        if (pos >= (s.size() / 2)) {
            return;
        }

        reverse_string_recursive(s, pos + 1);

        int lo = pos;
        int hi = (s.size() - 1) - pos;

        std::swap(s[lo], s[hi]);

        return;
    }


    /*
     * @brief reverses a string using recursion
     * 
     * @param s input vector of characters
     */
    void reverseString(vector<char>& s) {        
        if (s.size() == 0) {
            return;
        }

        reverse_string_recursive(s, 0);
    }
};


class Solution {
public:
     /*
      * @brief reverses a string iteratively
      * 
      * @param s
      */
    void reverseString(vector<char>& s) {
        size_t left = 0;
        size_t right = s.size() - 1;
        
        const size_t mid = s.size() / 2;
        
        for (size_t i = 0; i < mid; ++i) {
            char tmp = s[left];
            s[left]  = s[right];
            s[right] = tmp;
            
            ++left;
            --right;
        }
    }
};