#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a list is cycled
 * @list: parsed list
 * Return: 0 if a list is not cycled and 1 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);
	
	slow = list->next;

	fast = list->next->next;

	while (slow && fast && fast->next != NULL)
	{
		slow = slow->next;

		if (fast != NULL)
		{
			fast = fast->next->next;
			if (fast == list || fast == slow)
				return (1);
		}
	}

	return (0);
}
