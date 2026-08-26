#include <stdio.h>
#include <stdlib.h>

void printArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d\t", arr[i]);
    }
    printf("\n");
}

void insertionSort(int a[], int n)
{
    int key, j;
    for (int i = 1; i < n; i++) // for number of passes
    {
        key = a[i];
        j = i - 1;
        while (j >= 0 && a[j] > key) // for comparison in each pass
        {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;
    }
}  
int main()
{
    int arr[10] = {12, 3, 4, 2, 78, 67, 5, 54, 23, 65};
    int n=10;

    printArray(arr , 10);
    insertionSort(arr , 10);
    printArray(arr , 10);
    return 0;
}