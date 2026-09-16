#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int x,space;

    do
    {
        x = get_int("Height: ");
    }
    while ( x <= 0 || x > 8);

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

        printf("\n");
    }

    return 0;
}
