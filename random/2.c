#include <stdio.h>
#include <cs50.h>

int test(int x, int y, int z);

int main(void)
{
    int x = get_int("input first integer: ");
    int y = get_int("input second integer: ");
    int z = get_int("input third integer: ");
    if (test(x, y, z))
    {
        printf("%i\n", x);
    }
    else if (test(y, x, z))
    {
        printf("%i\n", y);
    }
    else if (test(z, x, y))
    {
        printf("%i\n", z);
    }
    return 0;
}

int test(int x, int y, int z)
{
    if ((x >= y && x <= z) || (x <= y && x >= z))
    {
        return 1;
    }
    else
    return 0;
}