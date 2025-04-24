#include <iostream>
#include <vector>
using namespace std;

int maxSubArray(vector<int> nums)
{
    int currentSum = 0;
    int maxSum = INT_MIN;

    for (int i : nums)
    {
        currentSum += i;
        maxSum = max(currentSum, maxSum);
        if (currentSum < 0)
        {
            currentSum = 0;
        }
    }
    return maxSum;
}
int main()
{

    vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int result = maxSubArray(nums);
    cout << result;

    return 0;
}