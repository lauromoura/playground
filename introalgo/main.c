#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <time.h>
#include "numgen.h"
#include "sorting.h"

void assert_sorted(int data[], const int len)
{
    int i;

    if (len == 0)
        return;

    if (len < 0) {
        perror("Invalid array length");
        abort();
    }
        

    for (i = 0; i < len - 1; i++) {
        assert (data[i] < data[i+1]);
    }
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

void run_test(int *data, const int num)
{
    clock_t start, diff;
    int msec = 0;
    if (!data) {
        perror("Invalid data for test.");
        abort();
    }

    start = clock();
    insertion_sort(data, num);
    diff = clock() - start;
    assert_sorted(data, num);
    
    msec = diff * 1000 / CLOCKS_PER_SEC;
    printf("Time taken: %d seconds %d milliseconds\n", msec/1000, msec%1000);
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
