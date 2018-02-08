#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

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

void fragment(int m)
{
    int ** ar1 = malloc(3 * m * sizeof(int *));
    int ** ar2 = malloc(m * sizeof(int *));
    int i, j;
    struct timespec alloc1_start, alloc1_end, alloc1, alloc2_start, alloc2_end, alloc2;
    //varaiable that is used just for adding up all the elments in the arrays
    int sum = 0;

    printf("Running fragment with m of value %d\n", m);
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &alloc1_start);
    for(i = 0; i < 3 * m; i++)
        ar1[i] = malloc(800000 * sizeof(int));
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &alloc1_end);
    alloc1 = diff(alloc1_start, alloc1_end);
    printf("Time1: %d seconds, %lu nanoseconds\n", alloc1.tv_sec, alloc1.tv_nsec);

    for(i = 0; i < 3 * m; i+=2)
        free(ar1[i]);

    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &alloc2_start);
    for(i = 0; i < m; i++)
        ar2[i] = malloc(900000 * sizeof(int));
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &alloc2_end);

    alloc2 = diff(alloc2_start, alloc2_end);
    printf("Time1: %d seconds, %lu nanoseconds\n", alloc2.tv_sec, alloc2.tv_nsec);


    for(i = 1; i < 3 * m; i+= 2)
        free(ar1[i]);
    for(i = 0; i < m; i++)
        free(ar2[i]);
}


int main(int argc, char * argv [])
{
    if(argc < 2){
        printf("Need to supply default value for m as a parameter\n");
        exit(1);
    }

    int m;
    char y [256];
    m = atoi(argv[1]);
    do{
        fragment(m);
        m *= 2;

        printf("Do you want to run again? ");
        fgets(y, 256, stdin);
    }while(y[0] == 'y');
    
    return 0;
}
