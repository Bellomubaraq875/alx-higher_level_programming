#include "lists.h"
/**
 * is_palindrome - This function checks if a singly linked list is a palindrome
 * @head: a pointer to the pointer containing the address of the first node
 * Return: 0 if not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *temp;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}
	if (fast != NULL)
		slow = slow->next;

	while (prev != NULL)
	{
		if (prev->n != slow->n)
		{
			is_palindrome = 0;
			break;
		}
		prev = prev->next;
		slow = slow->next;
	}
	prev = NULL;
	while (slow != NULL)
	{
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	(*head)->next = prev;

	return (is_palindrome);
}
