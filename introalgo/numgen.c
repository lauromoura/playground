#include "numgen.h"
#include <stdio.h>
#include <stdlib.h>

int *ordered_data(const int len)
{
    int i;
    int *data = NULL;

    if (len <= 0) {
        perror("Invalid size.\n");
        abort();
    }

    data = malloc(sizeof(int)*len);

    if (!data) {
        perror("Failed to allocate memory for data.\n");
        abort();
    }

    for (i = 0; i < len; i++) {
        data[i] = i;
    }

    return data;
}

int *reversed_data(const int len)
{
    int i;
    int *data = NULL;

    if (len <= 0) {
        perror("Invalid size.\n");
        abort();
    }

    data = malloc(sizeof(int)*len);

    if (!data) {
        perror("Failed to allocate memory for data.\n");
        abort();
    }

    for (i = 0; i < len; i++) {
        data[i] = len - i;
    }

    return data;
}

int *randomized_data(const int len)
{
    int i;
    int *data = NULL;

    if (len <= 0) {
        perror("Invalid size.\n");
        abort();
    }

    data = malloc(sizeof(int)*len);

    if (!data) {
        perror("Failed to allocate memory for data.\n");
        abort();
    }

    for (i = 0; i < len; i++) {
        data[i] = rand();
    }

    return data;
}

