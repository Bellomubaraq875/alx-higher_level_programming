#include "main.h"
/**
 * _strcat - This function concatenates two strings
 * @dest: a string
 * @src: another string
 * Return: dest
 */

char *_strcat(char *dest, char *src)
{
	int n = 0;
	char *o;

	o = dest;
	while (*dest)
	{
		dest++;
	}
	while (*(src + n))
	{
		*dest = *(src + n);
		dest++;
		n++;
	}
	*dest = *(src + n);
	while (dest != o)
	{
		dest--;
	}
	return (dest);
}
