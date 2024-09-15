#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts interger into the list
 * @head: head parsed
 * @number: number to be added
 * Return: new node address or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node, *temp, *new_node;
    listint_t *result = NULL;
    new_node = (listint_t *)malloc(sizeof(listint_t));
    if (new_node == NULL)
    {
        free(new_node);
        return (NULL);
    }
    new_node->n = number;
    
    if (*head == NULL)
    {
    	*head = new_node;
    	new_node->next = NULL;
    	return (new_node);
    }

    temp = *head;
    
    while (temp != NULL)
    {
    	if (temp->n > number)
    	{
    		*head = new_node;
    		new_node->next = temp;
    		return (new_node);
    	}
    	if (temp->next->n > number)
        {
            node = temp->next;
            temp->next = new_node;
            new_node->next = node;

            return (new_node);
        }
    	temp = temp->next;
    }

    if (temp->next == NULL)
    {
    	temp->next = new_node;
    	result = new_node;
    }
    return (result);
}