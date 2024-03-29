#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char** split_string(char*);

// Complete the sockMerchant function below.
int sockMerchant(int n, int ar_count, int* arr) {
    int freq[n];
    int check[n];
    int count, c = 0;
    for(int i = 0;i < n;i++){
        freq[i] = -1;
    }
    for(int i = 0;i < n;i++){
        count = 1;
        for(int j = i+1;j < n;j++){
            if(arr[i] == arr[j]){
                count++;
                freq[j] = 0;
            }
        }
        if(freq[i] != 0)
            freq[i] = count;
            check[c] = i;
            c++;
    }
    int pairs = 0;
    for(int i = 0;i < c;i++){
        pairs += freq[check[i]]/2;
    }
    return pairs;
}

int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    char* n_endptr;
    char* n_str = readline();
    int n = strtol(n_str, &n_endptr, 10);

    if (n_endptr == n_str || *n_endptr != '\0') { exit(EXIT_FAILURE); }

    char** ar_temp = split_string(readline());

    int* ar = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        char* ar_item_endptr;
        char* ar_item_str = *(ar_temp + i);
        int ar_item = strtol(ar_item_str, &ar_item_endptr, 10);

        if (ar_item_endptr == ar_item_str || *ar_item_endptr != '\0') { exit(EXIT_FAILURE); }

        *(ar + i) = ar_item;
    }

    int ar_count = n;

    int result = sockMerchant(n, ar_count, ar);

    fprintf(fptr, "%d\n", result);

    fclose(fptr);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);

    return data;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);
        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}
