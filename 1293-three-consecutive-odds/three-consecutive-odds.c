int compare(void *a, void *b){
   int k1 =  *((int*)(a));
   int k2 =  *((int*)(b));
   return k1 - k2;
}

bool threeConsecutiveOdds(int* arr, int arrSize) {
    //qsort(arr, arrSize, sizeof(int), compare);
    int a = 0;
    int prev = 0;
    if (arrSize <= 1) {
        return false;
    }
    for (int i = 0 ; i < arrSize ; i ++) {
        printf("%d\n", arr[i]);
        if (arr[i] % 2 != 0 ) {
                a ++;
        } else {
            a = 0;
        }
        if (a == 3) {
            return true;
        }
    }
    return false;
}