#include "lists.h"

/**
* check_cycle - checks if a singly linked list
* has a cycle in it
*
* @list: pointer to the head of the list
*
* Return: 0 in case a cycle was not found,
* and 1 if a cycle is found
*/

int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	while (hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
		{
			tortoise = list;
			while (tortoise != hare)
			{
				tortoise = tortoise->next;
				hare = hare->next;
			}
			return (1);
		}
	}

	return (0);
}
