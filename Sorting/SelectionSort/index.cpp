#include <iostream>
using namespace std;
int main()
{
    int arr[] = {9, 5, 7, 2, 6};
    int n = sizeof(arr) / 4;
    for (int i = 0; i < n; i++)
    {
        int min = INT_MAX;
        int minIndex = -1;
        for (int j = i; j < n; j++)
        {
            if (min>arr[j])
            {
                min = arr[j];
                minIndex = j;
            }
        }
        swap(arr[i], arr[minIndex]);
    }
    for (int i = 0; i < n; i++)
    {
        cout <<arr[i]<< " ";
    }
    return 0;
}
