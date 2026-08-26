#include<stdio.h>
#include<stdlib.h>

void print_array(int a[], int n)
{
    for(int i=0; i<n; i++)
    {
        printf("%d ", a[i]);
    }
    printf("\n");
}

int partition(int a[], int low, int high)
{
    int pivot=a[low];
    int i=low+1;
    int j=high;
    while (i<=j)
    {
        while (a[i] < pivot)
        {
            i++;
        }
        while (a[j] > pivot)
        {
            j--;
        }
        if (i<=j)
        {
            int temp=a[i];
            a[i]=a[j];
            a[j]=temp;
        }
    }
    int temp=a[low];
    a[low]=a[j];
    a[j]=temp;
    return j;    
}
void quicksort(int a[] , int low , int high)
{
    int partition_index;//index of pivot after partition
    
    if (low < high)
    {
        partition_index= partition(a , low , high);
        quicksort(a,low , partition_index-1);//sorting left subarray
        quicksort(a,partition_index+1, high);//sorting right subarray
    }
    
   
}
int main()
{
    int a[]= {3, 5 ,29 ,13 , 24 , 54};
    int n =6;

    print_array(a,n);
    quicksort(a,0,n-1);
    print_array(a,n);
return 0;
}