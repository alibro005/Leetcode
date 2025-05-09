#include <iostream>
using namespace std;
int main()
{
    int arr[] = {9, 3, 57, 3, 8, 5, 10};
    int n = sizeof(arr) / 4;

    for (int i = 0; i < n - 1; i++)
    {
        bool flag = true;
        for (int j = 0; j < n - 1 - i; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
                bool flag = false;
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    return 0;
}
