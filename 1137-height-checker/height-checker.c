
int comp (const void * elem1, const void * elem2) ;
int heightChecker(int* heights, int heightsSize) {
    int new_height[heightsSize];// = malloc(heightsSize*sizeof(int));
    for (int i = 0 ; i < heightsSize; i ++){
        new_height[i] = heights[i];
    }
   
    qsort (new_height, sizeof(new_height)/sizeof(*new_height), sizeof(*new_height), comp);

    int result = 0;

    for (int i = 0 ; i < heightsSize; i ++){
        printf("%d %d\n", new_height[i], heights[i]);
        if (new_height[i] != heights[i]) {
            result = result + 1;
        }
    }
    return result;

}

int comp (const void * elem1, const void * elem2) 
{
    int f = *((int*)elem1);
    int s = *((int*)elem2);
    if (f > s) return  1;
    if (f < s) return -1;
    return 0;
}