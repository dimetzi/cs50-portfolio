#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int min = 100;
    int number;
    do
    {
    number = get_int("how many integers do you want?: ");
    }
    while (number < 0 || number > 100);
    printf("Input the numbers:\n");
    for (int i = 0; i < number; i++)
    {
        int integer;
        do
        {
        integer = get_int("");
        }
        while (integer < 0);

        if (min > integer)
        {
            min = integer;
        }
    }
    printf("The smallest is %i\n", min);
}