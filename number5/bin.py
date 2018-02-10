import time

def binary_search(search, array):
    """ Iterative binary search funciton
    """
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
    """ performs 10000000 worst case binary searches for a given size and prints
        the time taken
    """
    num_times = 10000000
    t = time.time()
    for _ in range(num_times):
        binary_search(len(array), array)
    #time is in seconds so we multiply by 10**9 for nanoseconds
    t = (time.time() - t) * 10**9
    print("time taken for 10,000,000 worst case binary searches for arr "
          "of size {} => {} ns".format(len(array), t))

sizes = [128, 512, 2048, 8192, 32768, 131072, 524288, 2097152]
def main():
    """ Main function that performs worst case binary searches on all of 
        specified sizes
    """
    for size in sizes:
        run_test([i for i in range(size)])

if __name__ == '__main__':
    main()

