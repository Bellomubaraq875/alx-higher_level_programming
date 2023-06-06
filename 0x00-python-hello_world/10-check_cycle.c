#include "lists.h"
/**
* check_cycle - This function checks for cycles in a singly linked list
* @list: the list to be checked
* Return: 0 if there is no cycle or 1 if there is
*/
int check_cycle(listint_t *list)
{
	listint_t *List = list;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	while (list)
	{
		if (List == list)
		{
			return (1);
		}
		if (list->next->next == NULL)
		{
			return (0);
		}
		List = List->next;
		list = list->next->next;
	}
	return (0);
}
