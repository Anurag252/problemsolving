/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    *returnSize = 0;
    if (nums1Size > nums2Size) {
        *returnSize = nums1Size;
    } else {
        *returnSize = nums2Size;
    }

    int* arr = malloc(*returnSize * sizeof(int));
    int a = 0;
    for (int i = 0 ; i < nums1Size ; i ++) {
        for (int j = 0 ; j < nums2Size ; j ++) {
            if (nums1[i] == nums2[j]) {
                arr[a] = nums2[j];
                nums2[j] = -1;
                a ++ ;
                break;
            }
        }
    }
    *returnSize = a;
    return arr;
}