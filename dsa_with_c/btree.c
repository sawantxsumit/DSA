#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *left;
    struct node *right;
};
struct node *root;
struct node *insert(struct node *r, int datanode)
{
    if (r == NULL)
    {
        r = (struct node *)malloc(sizeof(struct node));
        r->data = datanode;
        r->left = NULL;
        r->right = NULL;
    }
    else if (datanode < r->data)
    {
        r->left = insert(r->left, datanode);
    }
    else
        r->right = insert(r->right, datanode);

    return r;
}

void inOrder(struct node *r)
{
    if (r != NULL)
    {
        inOrder(r->left);
        printf("%d ", r->data);
        inOrder(r->right);
    }
}

void preOrder(struct node *r)
{
    if (r != NULL)
    {
        printf("%d ", r->data);
        preOrder(r->left);
        preOrder(r->right);
    }
}

void postOrder(struct node *r)
{
    if (r != NULL)
    {
        postOrder(r->left);
        postOrder(r->right);
        printf("%d ", r->data);
    }
}
int main()
{
    root = NULL;
    int number, value;
    printf("enter the number of elements to be inserted :");
    scanf("%d", &number);
    for (int i = 0; i < number; i++)
    {
        printf("data number %d is ", i + 1);
        scanf("%d", &value);
        root = insert(root, value);
    }

    printf("\nINORDER TRAVERSAL \n");
    inOrder(root);
    printf("\n");

    printf("\nPREORDER TRAVERSAL \n");
    preOrder(root);
    printf("\n");

    printf("\nPOSTORDER TRAVERSAL \n");
    postOrder(root);
    printf("\n");

    return 0;
}