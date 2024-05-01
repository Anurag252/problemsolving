int missingNumber(int* nums, int numsSize) {
    int all_xor = 0 ;
    printf("%d", 1 ^ 1);
    for (int i = 0 ; i < numsSize; i ++) {
        all_xor = all_xor ^ *(nums + i) ^ i;
    }   

    // 3^0  ^ 0^1 ^ 1^2 ^ 3
    return all_xor ^ numsSize;
}