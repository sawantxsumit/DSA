#include<stdio.h>
#include<stdlib.h>

void print_array(int arr[], int n)
{
    for(int i=0; i<n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void selection_sort(int arr[], int n)
{
    int i, j, indexofmin, temp;
    for(i=0; i<n-1; i++)
    {
        indexofmin = i;
        for(j=i+1; j<n; j++)
        {
            if(arr[j] < arr[indexofmin])
            {
                indexofmin = j;
            }
        }
        temp = arr[i];
        arr[i] = arr[indexofmin];
        arr[indexofmin] = temp;
    }
}
int main()
{
    int arr[10] = {11 , 231 ,12, 23 ,16  , 23 ,  34 , 5, 6 ,1};
    print_array(arr, 10);
    selection_sort(arr, 10);
    print_array(arr, 10);

return 0;
}