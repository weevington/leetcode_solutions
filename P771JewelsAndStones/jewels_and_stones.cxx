class Solution {
public:
    /**
     *
     *  @param J std::string String containing jewels
     *  @param S std::string String containing stones
     */
    int numJewelsInStones(string J, string S) {
        uint32_t num_jewels = 0;
        std::set<char> J_set;

        /* iterate over jewels and add to set */
        std::string::const_iterator J_iter = J.cbegin();
        const std::string::const_iterator J_end  = J.cend();
        for (; J_iter != J_end; ++J_iter) {
            J_set.insert(*J_iter);
        }

         /* iterator over stones */
        std::string::const_iterator S_iter = S.cbegin(); 
        const std::string::const_iterator S_end = S.cend();
        const std::set<char>::const_iterator J_set_end = J_set.cend();
        for (; S_iter != S_end; ++S_iter) {
            if (J_set.find(*S_iter) != J_set_end) {
                ++num_jewels;
            }
        }

        return num_jewels;
    }
};