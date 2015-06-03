#include "util.h"
#include <stdio.h>

void dump_array(const int *data, const int num)
{
    int i;
    printf("{ ");
    for (i = 0; i < (num - 1); i++)
        printf("%d, ", data[i]);

    if (i != num)
        printf("%d ", data[i]);

    printf("}\n");
    return;
}
