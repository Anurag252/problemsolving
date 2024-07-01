
bool threeConsecutiveOdds(int* arr, int arrSize) {
    //qsort(arr, arrSize, sizeof(int), compare);
    int a = 0;
    int prev = 0;
   
    for (int i = 0 ; i < arrSize ; i ++) {
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