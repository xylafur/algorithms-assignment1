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
    t = time.clock()
    for _ in range(10000000):
        binary_search(len(array), array)
    t = time.clock() - t
    t *= (10 ** 9) # nano second conversion

    print('array size : %7d, time : %d ns' % (len(array), t))

>>>>>>> Stashed changes

def main():
    """ Main function that performs worst case binary searches on all of 
        specified sizes
    """
    sizes = [128, 512, 2048, 8192, 32768, 131072, 524288, 2097152]
    print("# Time taken to do 10000000 failed binary searches"
            +" for different array sizes.")
    for size in sizes:
        run_test([i for i in range(size)])

if __name__ == '__main__':
    main()

