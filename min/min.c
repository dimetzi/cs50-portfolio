// Practice writing a function to find a max value

#include <cs50.h>
#include <stdio.h>

int max(int array[], int n);

int main(void)
{
    int n;
    do
    {
        n = get_int("Number of elements: ");
    }
    while (n < 1);

    int arr[n];

    for (int i = 0; i < n; i++)
    {
        arr[i] = get_int("Element %i: ", i);
    }

    printf("The min value is %i.\n", max(arr, n));
}

// TODO: return the min value
int max(int array[], int n)
{
    int min_value = array[0];
    for (int i = 0; i < n; i++)
    {
        if (min_value > array[i])
        {
            min_value = array[i];
        }
    }
    return min_value;
}
