#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool check_char(string key);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key ");
        return 1;
    }
    if (!check_char(argv[1]))
    {
        printf("Key must contain 26 characters.");
        return 1;
    }
    string plaintext = get_string("Plaintext: ");
    int length = strlen(plaintext);
    string key = argv[1];
    char ciphertext[length + 1];
    for (int i = 0; i < length; i++)
    {
        if (isupper(plaintext[i]))
        {
            int index = plaintext[i] - 65;
            ciphertext[i] = key[index];
            if (islower(ciphertext[i]))
            {
                ciphertext[i] = ciphertext[i] - 32;
            }
        }
        else if (islower(plaintext[i]))
        {
            int index = plaintext[i] - 97;
            ciphertext[i] = key[index];
            if (isupper(ciphertext[i]))
            {
                ciphertext[i] = ciphertext[i] + 32;
            }
        }
        else
        {
            ciphertext[i] = plaintext[i];
        }
    }
    ciphertext[length] = '\0';
    printf("Ciphertext: %s\n", ciphertext);
}

bool check_char(string key)
{
    int length = strlen(key);

    if (length != 26)
    {
        return false;
    }
    for (int i = 0; i < length; i++)
    {
        key[i] = toupper(key[i]);
    }
    for (int i = 0; i < length; i++)
    {
        if (!isalpha(key[i]))
        {
            return false;
        }

        for (int j = 0; j < i; j++)
        {
            if (key[i] == key[j])
            {
                return false;
            }
        }
    }
    return true;
}