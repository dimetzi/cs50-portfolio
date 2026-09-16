#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int numbers = get_int("How many numbers: ");
    int sum = 0;
    int square = 0;
    printf("The squares are: ");
    for (int i = 1; i <= numbers; i++)
    {
        square = i * i;
        sum = sum + square;
        printf("%i ", square);
    }
    printf("\nThe sum of squares is: %i\n", sum);
}