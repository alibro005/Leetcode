#include <iostream>
using namespace std;
int mySqrt(int x)
{
    int start = 0, end = x;
    int ans = 0;

    while (start <= end)
    {
        long long mid = start + (end - start) / 2;
        if (mid * mid == x)
        {
            return mid;
        }
        else if (mid * mid > x)
        {
            end = mid - 1;
        }
        else
        {
            start = mid + 1;
        }
    }
}

int main()
{
    int x = 5;
    cout << mySqrt(x);
    return 0;
}