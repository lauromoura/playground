#include "sorting.h"
#include "util.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


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

void insert_first_sorted(int data[], int len)
{
    int value = 0;
    int i = 0;

    if (len == 0 || len == 1)
        return;

    for (i = 0; i < len - 1; i++) {
        int tmp;
        if (data[i] <= data[i+1])
            break;

        tmp = data[i+1];
        data[i+1] = data[i];
        data[i] = tmp;
    }
}

void insertion_sort_recursive(int data[], int len)
{
    if (len == 0)
        return;

    insertion_sort_recursive(data+1, len-1);
    insert_first_sorted(data, len);
}

static void merge(int data[], const int len, const int mid)
{
    int *left = NULL;
    int *right = NULL;
    int left_pos = 0;
    int right_pos = 0;
    int left_len = mid;
    int right_len = len - mid;
    int i = 0;

    if ((left = malloc(sizeof(int) * left_len)) == 0) {
        perror("Failed to allocate memory");
        abort();
    }
    if ((right = malloc(sizeof(int) * right_len)) == 0) {
        perror("Failed to allocate memory");
        abort();
    }

    left = memcpy(left, data, sizeof(int) * left_len);
    right = memcpy(right, data + mid, sizeof(int) * right_len);

    // Could have used MAX_INT as end of array flag, but it is also inside the
    // rand() return interval.
    for (i = 0; i < len; i++ ) {
        if (right_pos >= right_len) {
            // Empty right stack
            data[i] = left[left_pos++];
        } else if (left_pos >= left_len) {
            // Empty left stack
            data[i] = right[right_pos++];
        } else {
            // Both with itens
            if (left[left_pos] <= right[right_pos])
                data[i] = left[left_pos++];
            else
                data[i] = right[right_pos++];
        }
    }

    if (left)
        free(left);
    if (right)
        free(right);
}

void merge_sort(int data[], const int len)
{
    int left = 0;
    int mid = 0;

    if (len == 1)
        return;

    mid = len/2;

    merge_sort(data, mid);
    merge_sort(data + mid, len - mid);
    merge(data, len, mid);
}