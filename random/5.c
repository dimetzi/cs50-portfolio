#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int sum = 0;
    int numbers = get_int("How many numbers: ");
    printf("The natural numbers are: ");
    for (int i = 1; i <= numbers; i++)
    {
        sum = sum + i;
        printf("%i ", i);
    }
    printf("\nThe sum is: %i\n", sum);
}