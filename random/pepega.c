#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p;
    p = &n;
    printf("Adress: %p\n", &n);
    printf("Adress: %p\n", p);
}