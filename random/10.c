#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int size = get_int("Size: ");
    int f = 1;
    for (int i = 1; i <= size; i++)
    {
        f = f * i;
    }
    printf("%i\n", f);
}