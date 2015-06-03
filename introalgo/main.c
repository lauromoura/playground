#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include "numgen.h"
#include "sorting.h"
#include "util.h"

static int _compare_int(const void *a, const void *b)
{
    return (*(int*)a - *(int*)b);
}

void assert_sorted(int data[], const int len)
{
    int i;
    int *copy = NULL;

    if (len == 0)
        return;

    if (len < 0) {
        perror("Invalid array length");
        abort();
    }

    copy = malloc(sizeof(int)*len);

    if (!copy) {
        perror("Failed to allocate memory.");
        abort();
    }

    memcpy(copy, data, sizeof(int)*len);

    qsort(copy, len, sizeof(int), _compare_int);

    assert (memcmp(data, copy, sizeof(int)*len) == 0);

    free(copy);
}

/* FIXME Currently unused. */
int* load_data_prefix_num(const char* prefix, const int num)
{
    int i = 0;
    int* data = NULL;
    char buffer[1024];
    FILE* handle = NULL;

    data = malloc(sizeof(int) * num);
    if (!data) {
        perror("Failed to allocate memory.");
        abort();
    }

    snprintf(buffer, sizeof(buffer), "%s_%d.txt", prefix, num);
    if ((handle = fopen(buffer, "r")) == 0) {
        perror("Failed to open file.");
        abort();
    }

    for (i = 0; i < num; i++) {
        if (fscanf(handle, "%d", &(data[i])) == 0) {
            free(data);
            perror("Error reading numbers");
            abort();
        }
    }

    fclose(handle);

    return data;
}

void run_test_helper(int *data, const int num, void (*sort_function)(int*, const int))
{
    clock_t start, diff;
    int msec = 0;
    int *copy = NULL;

    if (!data) {
        perror("Invalid data for test.");
        abort();
    }

    if ((copy = malloc(sizeof(int)*num)) == 0) {
        perror("Failed to allocate memory.");
        abort();
    }

    memcpy(copy, data, sizeof(int)*num);

    start = clock();
    sort_function(copy, num);
    diff = clock() - start;
    assert_sorted(copy, num);
    
    msec = diff * 1000 / CLOCKS_PER_SEC;
    printf("Time taken: %d seconds %d milliseconds\n", msec/1000, msec%1000);

    free(copy);
}

void run_test(int *data, const int num)
{
    run_test_helper(data, num, insertion_sort);
}

int main(int argc, char* argv[])
{
    int *x = NULL;
    int len = 1000;

    srand(time(0));

    printf("Ordered test with %d numbers\n", len);
    x = ordered_data(len);
    run_test(x, len);
    free(x);

    printf("Random test with %d numbers\n", len);
    x = randomized_data(len);
    run_test(x, len);
    free(x);

    printf("Reversed test with %d numbers \n", len);
    x = reversed_data(len);
    run_test(x, len);
    free(x);

    return 0;
}
