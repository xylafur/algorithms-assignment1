import java.lang.management.*;

class Bin {
    final static int N_SEARCH = 10_000_000;

    static int binary_search(int search, int[] arr) {
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

    static void run_test(int ARR_SIZE) {
        int[] arr = new int[ARR_SIZE];
        for (int i = 0; i < ARR_SIZE; ++i) arr[i] = i;

        //long time = System.nanoTime();
        long time = check_cpu_time();
        for (int i = 0; i < N_SEARCH; ++i) {
            binary_search(ARR_SIZE, arr);
        }
        //time = System.nanoTime() - time;
        time = check_cpu_time() - time;

        System.out.printf(
            "array size : %7d, time : %d ns\n",
            ARR_SIZE, time);
    }

    static long check_cpu_time() {
        ThreadMXBean bean = ManagementFactory.getThreadMXBean();
        return bean.isCurrentThreadCpuTimeSupported()
            ? bean.getCurrentThreadCpuTime() : 0L;
    }

    public static void main(String[] args) {
        System.out.println(
            "# Time taken to do " + N_SEARCH
            + " failed binary searches different array sizes."
        );
        System.out.println("# Timed using Thread CPU Time executing code");

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

        for (int i : sizes) run_test(i);
    }

}

