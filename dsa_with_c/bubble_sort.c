#include <stdio.h>
#include <stdlib.h>

// we can make this bubble sort code adaptive
// it means that if the given array is already sorted then only one pass is required

int main()
{
  int arr[10] = {11, 22, 3, 54, 43, 1, 23, 44, 76, 12};

  int n = 1;
  int isSorted = 0;
  while (n < 10) // for number of passes
  {
    printf("pass no = %d \n", n);
    isSorted = 1;
    // this indicates the number of actual passes required to sort the array
    for (int i = 0; i < 10; i++) // for comparison
    {
      if (arr[i] > arr[i + 1])
      {
        int temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
        isSorted = 0;
      }
    }
    if (isSorted == 1)
    {
      break;
    }

    n++;
  }

  for (int i = 0; i < 10; i++)
  {
    printf("%d\t", arr[i]);
  }

  return 0;
}