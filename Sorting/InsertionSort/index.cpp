#include <iostream>
using namespace std;
int main()
{
    int arr[] = {29, 5, 8, 10, 2, 4};
    int n = sizeof(arr) / 4;

    for (int i = 0; i < n; i++)
    {
        int j = i + 1;
        while (j >= 1 && arr[j] < arr[j - 1])
        {
            swap(arr[j], arr[j - 1]);
            j--;
        }
    }

    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    return 0;
}
