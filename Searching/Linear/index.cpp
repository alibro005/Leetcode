#include <iostream>
using namespace std;
int main()
{
    int arr[] = {1, 10, 8, 6, 19, 29};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 6;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == target)
        {
            cout<< i;
        }
    }
    return 0;
}