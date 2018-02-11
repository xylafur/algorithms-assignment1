#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

/*  Function to get the difference between timespec structs
 */
struct timespec diff(struct timespec start, struct timespec end)
{
	struct timespec temp;
	if ((end.tv_nsec-start.tv_nsec)<0) {
		temp.tv_sec = end.tv_sec-start.tv_sec-1;
		temp.tv_nsec = 1000000000+end.tv_nsec-start.tv_nsec;
	} else {
		temp.tv_sec = end.tv_sec-start.tv_sec;
		temp.tv_nsec = end.tv_nsec-start.tv_nsec;
	}
	return temp;
}

/*  Function to fragment memory.
 */
void fragment(int m, int d, int e)
{
    int ** ar1 = malloc(3 * m * sizeof(int *));
    int ** ar2 = malloc(m * sizeof(int *));
    int i, j;
    struct timespec alloc1_start, alloc1_end, alloc1, alloc2_start, alloc2_end, alloc2;
    //varaiable that is used just for adding up all the elments in the arrays
    int sum = 0;

    printf("Running fragment with m of value %d\n", m);
    printf("First allocation\n");
    if(!e)
        clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &alloc1_start);
    for(i = 0; i < 3 * m; i++){
        if(e && (i <= 10 || i >= (3 * m - 10)))
            clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &alloc1_start);
        ar1[i] = malloc(800000 * sizeof(int));
        if(ar1[i] == 0){
            printf("Error, malloc failed\n");
            exit(1);
        }
        if(e && (i <= 10 || i >= (3 * m - 10))){
            clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &alloc1_end);
            alloc1 = diff(alloc1_start, alloc1_end);
            printf("Time1 i = %d: %d seconds, %lu nanoseconds\n", i, alloc1.tv_sec, alloc1.tv_nsec);
        }
    }
    if(!e){
        clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &alloc1_end);
        alloc1 = diff(alloc1_start, alloc1_end);
        printf("Time1: %d seconds, %lu nanoseconds\n", alloc1.tv_sec, alloc1.tv_nsec);
    }

    for(i = 0; i < 3 * m; i+=2)
        free(ar1[i]);

    printf("Second allocation\n");
    if(!e)
        clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &alloc2_start);
    for(i = 0; i < m; i++){
        if(e && (i <= 10 || i >= m - 10))
            clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &alloc2_start);
        ar2[i] = malloc(900000 * sizeof(int));
        if(ar2[i] == 0){
            printf("Error, malloc failed\n");
            exit(1);
        }
        if(e && (i <= 10 || i >= m - 10)){
            clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &alloc2_end);
            alloc2 = diff(alloc2_start, alloc2_end);
            printf("Time2 i = %d: %d seconds, %lu nanoseconds\n", i, alloc2.tv_sec, alloc2.tv_nsec);
        }
    }

    printf("\n");

    if(!e){
        clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &alloc2_end);
        alloc2 = diff(alloc2_start, alloc2_end);
        printf("Time1: %d seconds, %lu nanoseconds\n", alloc2.tv_sec, alloc2.tv_nsec);
    }

    if(d){
        printf("Addresses for array 1\n");
        for(i = 0; i < 3 * m; i++){
                printf("%lu, ", ar1[i]);
                if(i % 10 == 0)
                    printf("\n");
        }
        printf("Addresses for array 2\n");
        for(i = 0; i < m; i++){
                printf("%lu, ", ar2[i]);
                if(i % 10 == 0)
                    printf("\n");
        }
    }
    exit(1);

    for(i = 1; i < 3 * m; i+= 2)
        free(ar1[i]);
    for(i = 0; i < m; i++)
        free(ar2[i]);
    free(ar1);
    free(ar2);
}


int main(int argc, char * argv [])
{
    if(argc < 2){
        printf("Need to supply default value for m as a parameter\n");
        exit(1);
    }
    int m, d = 0, e = 0;
    char y [256];

    if(argc >= 3)
        d = 1;
    if(argc == 4)
        e = 1;
    

    m = atoi(argv[1]);
    do{
        fragment(m, d, e);
        m++;
        break;
    }while(0);
    
    return 0;
}
