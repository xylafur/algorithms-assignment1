
class Bin {
    static int NSEARCH = 10000000;
    private static int binary_search(int search, int[] arr) {
        int start = 0, end = arr.length - 1, mid = (start + end) / 2;
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

    private static void run_test(int ARR_SIZE) {
        int[] arr = new int[ARR_SIZE];
        for (int i = 0; i < ARR_SIZE; ++i) {
            arr[i] = i;
        }

        long time = System.nanoTime();
        for (int i = 0; i < NSEARCH; ++i) {
            binary_search(ARR_SIZE, arr);
        }
        time = System.nanoTime() - time;

        System.out.printf("Time taken to do %d failed binary searches for array"
                          +" of size %d : %d nanoseconds\n",
                          NSEARCH, ARR_SIZE, time);
    }

    public static void main(String[] args) {
        int[] sizes = {
            128,
            512,
            2048,
            8912,
            32768,
            131072,
            524288,
            2097152,
        };

        for (int i = 0; i < sizes.length; ++i) {
            run_test(sizes[i]);
        }
    }

}
