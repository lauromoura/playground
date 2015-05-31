#include "sorting.h"

void insertion_sort(int data[], const int len)
{
    int i;
    int j;
    for (i = 1; i < len; i++)
    {
        for (j = i; j > 0 && data[j-1] > data[j]; j--) {
            int temp;
            temp = data[j];
            data[j] = data[j-1];
            data[j-1] = temp;
        }
    }
}

