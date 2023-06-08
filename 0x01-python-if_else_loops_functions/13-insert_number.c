#include "lists.h"

/**
* insert_node - This inserts a number into a sorted singly linked list
* @head: pointer to the pointer to the first address
* @number: the number to be inserted
* Return: address of the new node or NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	int n;
	listint_t *current;
	(void)n;

	current = *head;
	current = malloc(sizeof(listint_t));
	if (current == NULL)
		return (NULL);
	if (*head == NULL)
	{
		return (NULL);
	}
	if (!number)
	{
		return (NULL);
	}
	while (head != NULL)
	{
		current->n = number;
	}
	return (*head);
}
