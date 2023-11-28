#include "lists.h"

/**
  * check_cycle -  find the loop
  * @head: head
  * Return: start point int the loop
  */
int check_cycle(listint_t *head)
{
	listint_t *fast = head, *slow = head;

	if (head == NULL)
		return (0);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			break;
		}
	}
	if (!(slow && fast && fast->next))
		return (0);
	if (slow == fast)
	{
		slow = head;
	}
	while (slow != fast)
	{
		slow = slow->next;
		fast = fast->next;
	}
	return (1);
}
