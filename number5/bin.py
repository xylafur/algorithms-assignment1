
import time

def binary_search(search, array):
    start, end = 0, len(array)-1
    mid = (start + end) // 2
    while start < end:
        if array[mid] == search:
            return mid
        if search < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2
    return -1

def run_test(array):
    t = time.time()
    for _ in range(10000000):
        binary_search(len(array), array)
    t = time.time() - t
    print('10,000,000 bin_search for arr[{}] => {} ns'.format(len(array), t))

sizes = [128, 512, 2048, 8192, 32768, 131072, 524288, 2097152]
def main():
    for size in sizes:
        run_test([i for i in range(size)])

if __name__ == '__main__':
    main()

