#include "lists.h"
/**
  * reverse_listint - reverse the linked list
  * @head: the head
  * Return: pointer the head
  */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *next_node = *head, *pre_node = NULL;

	while (*head)
	{
		next_node = (*head)->next;
		(*head)->next = pre_node;
		pre_node = *head;
		*head = next_node;
	}
	*head = pre_node;

	return (*head);
}
/**
  * is_palindrome - check if the list is palindrome
  * @head: listint_t
  * Return: 0 if not palindrome 1 else
  */
int is_palindrome(listint_t **head)
{
	listint_t *left, *right, *current;
	int len = 0, mid, upper, i = 0;

	/* empty list is a palindrome */
	if (!head)
		return (0);
	/* size of the linked list */
	current = *head;
	while (current != NULL)
	{
		current = current->next;
		len++;
	}
	mid = len / 2;
	if (len % 2 == 0)
		upper = mid;
	else
		upper = mid + 1;
	/* find the right half of the list */
	right = *head;
	while (i != upper)
	{
		right = right->next;
		i++;
	}
	/* reverse the right list */
	reverse_listint(&right);
	/* check if the list is a palindrome */
	left = *head;
	i = 0;
	while (i < mid)
	{
		if (left->n != right->n)
			return (0);
		left = left->next;
		right = right->next;
		i++;
	}
	return (1);
}
