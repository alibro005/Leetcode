#include <iostream>
using namespace std;
int main()
{
    int arr[] = {1, 3, 6, 7, 8, 9, 19};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 9;
    int start = 0, end = n - 1;
    while (start <= end)
    {
        int mid = start + (end - start) / 2;
        if (target > arr[mid])
        {
            start = mid + 1;
        }
        else if (target < arr[mid])
        {
            end = mid - 1;
        }
        else
        {
            cout << mid;
            break;
        }
    }

    return 0;
}