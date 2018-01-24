import time

def binary_search(array, bottom, top, search):
    if bottom >= top:
        return None
    index = (top + bottom) // 2
    val = array[index] 
    if val == search:
        return index
    if val < search:
        return binary_search(array, index+ 1, top, search)
    if val > search:
        return binary_search(array, bottom, index - 1, search)

def timer(function, *args, **kwargs):
    start = time.time()
    function(*args, **kwargs)
    end = time.time()
    return end-start

def average_time(iterations, function, *args, **kwargs):
    total = 0
    for _ in range(iterations):
        total += timer(function, *args, **kwargs)
    return total / iterations

def populate_list(list, size):
    for i in range(size):
        list.append(i)

sizes = [128, 512, 2048, 8192, 32768, 131072, 524288, 2097152]
def main():
    for size in sizes:
        list = []
        populate_list(list, size)
        avg_time = average_time(10000000, binary_search, list, 0, len(list) - 1, size)
        print("{} => {}".format(size, avg_time))
        size *= 2
    
if __name__ == '__main__':
    main()

        
