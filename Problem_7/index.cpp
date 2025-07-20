#include <iostream>
using namespace std;

int reverse(int x)
{
    int reversed = 0;

    while (x != 0)
    {
        int last_digit = x % 10;
        reversed = reversed * 10 + last_digit;
        x /= 10;
    }

    if ((reversed > INT_MAX / 10) || (reversed < INT_MIN / 10))
    {
        return 0;
    }
    return reversed;
}

int main()
{
    int x = -123;
    cout << reverse(x);
    return 0;
}