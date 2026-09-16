#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int numbers = get_int("How many numbers: ");
    for (int i = 1; i <= numbers; i++)
    {
        int j = i*i*i;
        printf("%i\n", j);
    }
}