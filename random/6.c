#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int sum = 0;
    float average = 0;
    int numbers;
    for (int i = 1; i <= 10; i++)
    {
        numbers = get_int("Natural number%i: ", i);
        sum = sum + numbers;
    }
    average = sum / 10.0;
    printf("\nThe sum is: %i\nThe average is: %.2f\n", sum, average);
}