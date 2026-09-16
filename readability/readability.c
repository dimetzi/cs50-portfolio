#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>


int main(void)
{
    string text = get_string("Text: ");
    int word = 0;
    int letter = 0;
    int sentence = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isupper(text[i]) || islower(text[i]))
        {
            letter++;
        }
        if (isspace(text[i]))
        {
            word++;
        }
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentence++;
        }
    }
    float L = letter / (float) word *100;
    float S = sentence / (float) word *100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

