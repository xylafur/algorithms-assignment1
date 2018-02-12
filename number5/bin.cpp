
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <chrono>
using namespace std;
using namespace std::chrono;

#define NSEARCH 10000000

int binary_search(const int search, int * arr, const size_t size) {
    int start = 0, end = size - 1, mid = (start + end) / 2;
    while (start < end) {
        if (search == arr[mid]) return search;

        if (arr[mid] < search) {
            start = mid + 1;
        } else { // arr[mid] > search
            end = mid - 1;
        }
        mid = (start + end) / 2;
    }
    return -1;
}

void run_test(size_t ARR_SIZE) {
    int * arr = new int[ARR_SIZE];
    for (size_t i = 0; i < ARR_SIZE; ++i) {
        arr[i] = i;
    }

    auto t1 = high_resolution_clock::now();
    for (int i = 0; i < NSEARCH; ++i) {
        binary_search(ARR_SIZE, arr, ARR_SIZE);
    }
    auto t2 = high_resolution_clock::now();

    auto time = duration_cast<std::chrono::nanoseconds>(t2 - t1).count();

    printf("array size : %7d, time : %d ns\n",
            ARR_SIZE, time);

//    delete[] arr; // clean up
}

int main(int argc, char ** argv) {
    size_t sizes[] = {
        128,
        512,
        2048,
        8912,
        32768,
        131072,
        524288,
        2097152,
    };

    cout << "# Time taken to do " << NSEARCH << " failed binary searches"
         << " for different array sizes. " << endl;

    for (int i = 0; i < 8; ++i) {
        run_test(sizes[i]);
    }

    return 0;
}


