#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int x = get_int("x= ");
    int y = get_int("y= ");

    if (x == y)
    {
        int sum = x + y;
        return sum * 3;
    }
    else
    return 0;
}