#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Asks for Name and say hello 
    string name = get_string("What's your name?\n ");
    printf("hello, %s\n", name);
}