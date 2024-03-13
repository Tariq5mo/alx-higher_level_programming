#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 *
 * @head: The head pointer.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *head)
{
	listint_t *p;
	int i;

	if (!head)
		return (0);
	while (head)
	{
		p = head;
		i = 100;
		while (i > 0)
		{
			if (p)
				p = p->next;
			if (p == head)
				return (1);
			else if (!p)
				return (0);
			i--;
		}
		head = head->next;
	}
	return (0);
}
