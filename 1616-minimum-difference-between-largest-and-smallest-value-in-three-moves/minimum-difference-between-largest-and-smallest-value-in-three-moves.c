int compare(void* a, void* b){
   int k1 =  *((int*)(a));
   int k2 = *((int*)(b));
   return k2-k1;
}

int MIN(int a, int b){
    if (a < b){
        return a;
    }
    return b;
}

int minDifference(int* nums, int numsSize) {
   qsort(nums, numsSize, sizeof(int), compare);

    if (numsSize <= 4){
        return 0;
    }
    int result = INT_MAX;
    for (int i = 0 ; i + numsSize -4 < numsSize; i ++){
        result = MIN(result, nums[i] - nums[i + numsSize -4]);
    }
    return result;
    
}
//95,82,81,75,20