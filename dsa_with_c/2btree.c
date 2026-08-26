#include <stdio.h>
#include <stdlib.h>

/*
this code includes :-

node creation
preorder traversal
postorder traversal
inorder traversal
checking if a tree is bst or not
searching in a binary tree using recursion
searching in a binary tree using iteration
inserting in a bst
deletion in a bst
*/
struct node
{
    int data;
    struct node *left;
    struct node *right;
};

struct node *createnode(int val)
{
    struct node *q;
    q = (struct node *)malloc(sizeof(struct node));
    q->data = val;
    q->left = NULL;
    q->right = NULL;

    return q;
}

void preorder(struct node *root)
{
    if (root != NULL)
    {
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

void postorder(struct node *root)
{
    if (root != NULL)
    {
        postorder(root->left);
        postorder(root->right);
        printf("%d ", root->data);
    }
}
void inorder(struct node *root)
{
    if (root != NULL)
    {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

int isBST(struct node *root)
{
    static struct node *prev = NULL;
    if (root != NULL)
    {
        if (!isBST(root->left))
        {
            return 0;
        }
        if (prev != NULL && root->data <= prev->data)
        {
            return 0;
        }
        prev = root;
        return isBST(root->right);
    }
    else
        return 1;
}

struct node *search(struct node *root, int key)
{ // searching in a binary tree using recursion
    if (root == NULL)
    {
        return NULL;
    }
    if (key == root->data)
    {
        return root;
    }

    else if (key < root->data)
    {
        return search(root->left, key);
    }
    else
    {
        return search(root->right, key);
    }
}

// searching in a binary tree using iteration
struct node *searchITR(struct node *root, int key)
{
    while (root != NULL)
    {
        if (key == root->data)
        {
            return root;
        }
        else if (key < root->data)
        {
            root = root->left;
        }
        else
        {
            root = root->right;
        }
    }
    return NULL;
}

void *insert(struct node *root, int key)
{

    if (root == NULL)
    {
        root = createnode(key);
    }

    else if (key < root->data)
    {
        root->left = insert(root->left, key);
    }
    else
    {
        root->right = insert(root->right, key);
    }
    return root;
}
struct node *inorderpredecessor(struct node *root)
{
    root = root->left;
    while (root->right != NULL)
    {
        root = root->right;
    }
    return root;
}

struct node *deleteNode(struct node *root, int value)
{
    struct node *ipre;
    if (root == NULL)
    {
        return NULL;
    }
    if (root->left == NULL && root->right == NULL)
    {
        free(root);
        return NULL;
    }

    // search for the node
    if (value < root->data)
    {
        root->left = deleteNode(root->left, value);
    }
    else if (value > root->data)
    {
        root->right = deleteNode(root->right, value);
    }
    else
    {
        ipre = inorderpredecessor(root);
        root->data = ipre->data;
        root->left = deleteNode(root->left, ipre->data);
    }

    return root;
}
int main()
{
    struct node *p = createnode(9);
    struct node *p1 = createnode(2);
    struct node *p2 = createnode(12);
    struct node *p3 = createnode(0);
    struct node *p4 = createnode(5);
    struct node *p5 = createnode(11);
    struct node *p6 = createnode(16);

    // tree
    /*       4
           /   \
          1     6
         / \
        5   2
    */
    p->left = p1;
    p->right = p2;
    p1->left = p3;
    p1->right = p4;
    p2->left = p5;
    p2->right = p6;

    printf(" \n PREORDER TRAVERSAL \n");
    preorder(p);
    printf(" \n INORDER TRAVERSAL \n");
    inorder(p);
    printf(" \n POSTORDER TRAVERSAL \n");
    postorder(p);
    printf("\n");
    printf("%d\n", isBST(p)); // return 1 for bst and 0 for not bst

    struct node *n = search(p, 12);
    if (n != NULL)
    {
        printf(" found %d \n", n->data);
    }
    else
    {
        printf("element not found ");
    }

    struct node *t = searchITR(p, 12);
    if (t != NULL)
    {
        printf(" found %d \n", t->data);
    }
    else
    {
        printf("element not found ");
    }

    // insert(p , 6);
    //  printf(" \n PREORDER TRAVERSAL \n");
    // preorder(p);

    deleteNode(p, 5);  // not working for 5 after inserting 6
    printf(" \n after deletion \nPREORDER TRAVERSAL \n");
    preorder(p);
    printf(" \n INORDER TRAVERSAL \n");
    inorder(p);
    printf(" \n POSTORDER TRAVERSAL \n");
    postorder(p);
    printf("\n");

   
    return 0;
}