

#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>


void f(std::vector<int> &temp,
       std::vector<std::vector<int> > &result,
       int i,
       const std::vector<int> &nums);

void
get_superset(std::vector<std::vector<int> > superSet,
             std::vector<int> rem,
             int index,
             std::vector<int> originalSet);


void f(std::vector<int> &temp,
       std::vector<std::vector<int> > &result,
       int i,
       const std::vector<int> &nums)
{
    if (i == nums.size()) {
        result.push_back(temp);
        return;
    }

    temp.push_back(nums[i]);
    f(temp, result, i + 1, nums);
    temp.pop_back();
    std::cout << "popping back, tmp.size() = " << temp.size() << "i = " << i << std::endl;
    std::cout << "calling f with val " << i << " + 1 = " << i + 1 << std::endl;
    f(temp, result, i + 1, nums);

}


void
get_superset(std::vector<std::vector<int> > superSet,
             std::vector<int> rem,
             int index,
             std::vector<int> originalSet)
{


}


void
subsets(const std::vector<int> &nums)
{

    std::vector<std::vector<int> > superset;
    std::vector<int> temp;


    std::vector<int> sortednums = nums;
    std::sort(sortednums.begin(), sortednums.end());

    const std::vector<int> snums = sortednums;

    //get_superset(superset, temp, 0, nums);
    f(temp, superset, 0, snums);

    for (int k = 0; k < superset.size(); ++k) {
        std::cout << "[";
        for (size_t m = 0; m < superset.at(k).size(); ++m) {
            std::cout << superset.at(k).at(m);
            std::cout << ", ";
        }
        std::cout << "]";
        std::cout << ",";
    }

    std::cout << std::endl;

}


int main(int argc, char *argv[])
{
    std::vector<int> myset;

    myset.push_back(1);
    myset.push_back(2);
    myset.push_back(3);

    subsets(myset);

    return EXIT_SUCCESS;
}