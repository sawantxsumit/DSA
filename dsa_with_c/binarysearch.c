#include <stdio.h>
#include <stdlib.h>

int binarySearch(int arr[], int high, int low, int target)
{
      while (low <= high)
      {
        int mid = (low + high) / 2;
        if (arr[mid] == target)
        {
            return mid;
        }
        else if (arr[mid] > target)
        {
            high= mid -1;
        }
        else 
        {
            low=mid+1;
        }
      }
    return 0;
}
int main()
{
    int arr[10] = {1, 2, 3,  4, 5, 6, 7, 8, 9, 10};
    int target = 9;

    int res = binarySearch(arr, 9, 0, target);
    if (res == 0)
    {
        printf("element not found ");
    }
    else
    {
        printf("the element is found at index %d ", res);
    }

    return 0;
}