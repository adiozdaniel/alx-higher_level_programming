#include "lists.h"

/**
* insert_node - Inserts a number into a sorted singly-linked list
* @head: A pointer to the head of the linked list
* @number: The number to insert
*
* Return: A pointer to the new node, or NULL in case of failure
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	/* Allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	/* Initialize the new node */
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{/* Insert a new node if list is empty */
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current = *head;/* Traverse the list to find the insertion point */
	while (current->next != NULL && current->next->n < number)
		current = current->next;

	new_node->next = current->next;/* Insert the new node into the list */
	current->next = new_node;

	return (new_node);
}
