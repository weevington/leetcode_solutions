class Solution {
public:
    /**
     *  @param nums std::vector<int>
     *  Determines 
     */
    int singleNumber(vector<int>& nums) {
        std::unordered_map<int, int> count_map;

        std::vector<int>::iterator nums_iter = nums.begin();
        const std::vector<int>::const_iterator nums_end  = nums.end();

        const std::unordered_map<int, int>::const_iterator
            count_end = count_map.cend();
        
        for (; nums_iter != nums_end; ++nums_iter) {
            if (count_map.find(*nums_iter) == count_end) {
                count_map[*nums_iter] = 1;
            } else{
                count_map[*nums_iter] += 1;
            }
        }

        std::unordered_map<int, int>::const_iterator
            count_iter = count_map.cbegin();
        for (; count_iter != count_end; ++count_iter) {
            if (count_iter->second == 1) {
                return count_iter->first;
            }
        }
        
        return -1;

    }
};