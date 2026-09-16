#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x, space;

    do
    {
        x = get_int("Size: ");
    }
    while (x < 1 || x > 8);

    for (int i = 0; i < x; i++)
    {
        for (space = 0; space < x - i - 1; space++)
        {
            printf(" ");
        }
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("  ");
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }

        printf("\n");
    }

    return 0;
}