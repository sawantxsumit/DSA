#include<stdio.h>
#include<stdlib.h>

void print_array(int arr[], int n )
{
    for(int i=0; i<n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
void merge(int arr[], int mid, int low, int high)
{
    int i , j ,k , b[100];
    i=low;
    j=mid+1;
    k=low;
    while (i<=mid && j<=high)   
    {
        if (arr[i]< arr[j]) 
        {
            b[k] = arr[i];
            i++;
            k++;
        }
        else
        {
            b[k] = arr[j];
            j++;
            k++;
        }  
    }
    while (i<=mid)
    {
        b[k] = arr[i];
        k++;
        i++;
    }
    while (j<=high)
    {
        b[k] = arr[j];
        k++;
        j++;
    }  
    for (int i = low; i <= high; i++)
    {
        arr[i] = b[i];
    }
     
}
void merge_sort(int arr[],int low, int high)
{
    if (low<high)
    {
        int mid = (low+high)/2;
        merge_sort(arr, low, mid);
        merge_sort(arr, mid+1, high);
        merge(arr, mid, low , high);
    }
}
int main()
{
   int arr[10] = {11 , 231 ,12, 23 ,16  , 23 ,  34 , 5, 6 ,1};
    print_array(arr, 10);
    merge_sort(arr,0, 9);
    print_array(arr, 10); 
return 0;
}