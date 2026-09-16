#include <stdio.h>

int main(void)
{
    int sum = 0;
    printf("The natural numbers are: ");
    for (int i = 1; i <= 10; i++)
    {
        sum = sum + i;
        printf("%i ", i);
    }
    printf("\nThe sum is: %i\n", sum);
}