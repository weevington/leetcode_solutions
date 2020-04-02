
#include <iostream>
#include <vector>

class Solution {
public:
    void mergePreSortedArrays(const std::vector<int> &arrayA,
                              const std::vector<int> &arrayB,
                              std::vector<int> &arrayC)
    {
        int indexA = 0;
        int indexB = 0;
        int indexC = 0;

        while((indexA < static_cast<int>(arrayA.size())) &&
              (indexB < static_cast<int>(arrayB.size())))
        {
            if (arrayA.at(indexA) < arrayB.at(indexB))
            {
                arrayC.at(indexC) = arrayA.at(indexA);
                indexA++;    //increase the subscript
            } else {
                arrayC.at(indexC) = arrayB.at(indexB);
                indexB++;
            }
            indexC++; //move to the next position in the new array
        }

        // Move remaining elements to end of new array when one merging array is empty
        while (indexA < static_cast<int>(arrayA.size()))
        {
            arrayC.at(indexC) = arrayA.at(indexA);
            indexA++;
            indexC++;
        }
        while (indexB < arrayB.size())
        {
            arrayC.at(indexC) = arrayB.at(indexB);
            indexB++;
            indexC++;
        }

        return;
    }

    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        std::vector<int> merged(nums1.size() + nums2.size(), 0);

        mergePreSortedArrays(nums1,
                             nums2,
                             merged);

        //std::cout << "merged.size() = " << merged.size();

        if (merged.size() % 2 == 0) {
            return (merged.at(merged.size() / 2 - 1) + merged.at((merged.size() / 2))) / 2.;
        } else {
            return merged.at((merged.size() / 2));
        }

    }
};


int main(int argc, char *argv[])
{

    Solution sol;

    std::vector<int> v1 = {};
    std::vector<int> v2 = {};

    double med = sol.findMedianSortedArrays(vOne,
                                            vTwo);

    std::cout << " median is equal to " << med << std::endl;

    return EXIT_SUCCESS;
}