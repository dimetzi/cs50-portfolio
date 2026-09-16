#include <stdio.h>
#include <cs50.h>


int main(void)
{
    int height = get_int("Height: ");
    
    if (height <= 0)
    {
        return 0;
    }

    draw(height - 1);

    for (int i = 0; i <height; i++)
    {
        printf("#");
    }
    printf("\n");
}