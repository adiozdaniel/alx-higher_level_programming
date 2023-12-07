#include <stdio.h>
#include <string.h>

#define PASSWORD_LENGTH 20

/**
* generate_key - Generates a valid key for the given username.
*
* @username: The username for which the key needs to be generated.
* @key: Pointer to the buffer to store the generated key.
*/
static void generate_key(const char *username, char *key)
{
	/* Example key generation logic: Concatenate username with a secret string */
	const char *secret = "julien";

	strcpy(key, username);
	strcat(key, "_");
	strcat(key, secret);
}

/**
* main - Main function for the key generation.
* @argc: Number of arguments
* @argv: Array of
* Return: 0 upon successful completion.
*/
int main(int argc, char *argv[])
{
	const char *username;

	if (argc != 2)
	{
		fprintf(stderr, "Usage: %s <username>\n", argv[0]);
		return (1);
	}

	username = argv[1];

	{
		char key[PASSWORD_LENGTH + 1];

		generate_key(username, key);

		/* Print the generated key */
		printf("%s\n", key);
	}

	return (0);
}
