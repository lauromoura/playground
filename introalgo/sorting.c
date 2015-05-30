#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <errno.h>

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

void run_test(const char* prefix, const int num)
{
    int *data = NULL;
    data = load_data_prefix_num(prefix, num);

    if (!data) {
        perror("Failed to load file.");
        abort();
    }
    insertion_sort(data, num);
    assert_sorted(data, num);

    free(data);
}

int main(int argc, char* argv[])
{
    int data[] = {4, 3, 2, 1};
    int *x = NULL;
    int len = 4;
    insertion_sort(data, len);
    assert_sorted(data, len);

    len = 1000;
    printf("Ordered test with %d numbers\n", len);
    run_test("ordered", len);
    printf("Random test with %d numbers\n", len);
    run_test("random", len);
    printf("Reversed test with %d numbers \n", len);
    run_test("reverse", len);
    
    return 0;
}
