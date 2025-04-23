#include <iostream>
using namespace std;

bool isPalindrome(int x)
{

    if (x < 0)
    {
        return false;
    }

    long long reversed = 0;
    int orignal = x;

    while (x != 0)
    {

        int last_digit = x % 10;
        reversed *= 10;
        reversed += last_digit;
        x /= 10;
    }
    return orignal == reversed;
}

int main()
{
    int x = 121;
    cout << isPalindrome(x);
    return 0;
}