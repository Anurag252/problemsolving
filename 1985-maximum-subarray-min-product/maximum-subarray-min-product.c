
struct Node;
typedef struct Node *PtrToNode;
typedef PtrToNode Stack;

struct Node
{
    long Element;
    long index;
    PtrToNode Next;
};

bool IsEmpty(Stack S);
Stack CreateStack(void);
void Push(long X, long index, Stack S);
Stack  Pop(Stack S);

int maxSumMinProduct(int* nums, int numsSize) {
    long sumleft[numsSize];
    long sum_left = 0;
    long sumRight[numsSize];
    long sum_right = 0;
    long totalSum = 0;
    long leftMin[numsSize];
    long left_min = 0;
    long rightMin[numsSize];
    long right_min = numsSize - 1;

    long result = 0;

    for (int i = 0 ; i < numsSize; i ++ ){
        //printf("%d kk--", i);
        totalSum = totalSum + *(nums + i);
        
        sum_left = sum_left + *(nums + i);
        sumleft[i] = sum_left;

        sum_right = sum_right + *(nums + numsSize - i-1);
        sumRight[numsSize - i-1] = sum_right;
    }

    Stack S = CreateStack();
    for (int i = 0; i < numsSize ; i ++) {
        //printf("%d ----", i);
        if (!IsEmpty(S) && S -> Next -> Element > *(nums + i)){
            while ( !IsEmpty(S) && S ->Next -> Element > *(nums + i) ) {
             Stack tmp = Pop(S);
             rightMin[tmp -> index] = i;
             free(tmp);
            }
            rightMin[i] = numsSize ;
            Push(*(nums + i), i, S);
        } else {
            Push(*(nums + i), i, S);
            rightMin[i] = numsSize ;
        }
    }
     
    S = CreateStack();
     for (int i = numsSize-1; i >= 0 ; i --) {
        if (!IsEmpty(S) && S ->Next-> Element > *(nums + i)) {
            //printf("\n%d --vvv---\n", S -> Next -> Element);
            while (!IsEmpty(S) && S ->Next -> Element > *(nums + i) ) {
            Stack tmp = Pop(S);
            leftMin[tmp -> index] = i;
            free(tmp);
            }
            leftMin[i] = -1;
            Push(*(nums + i), i, S);
        } else {
            //printf("\n%d --v1v1v1---%d\n", *(nums + i), i);
            Push(*(nums + i), i, S);
            leftMin[i] = -1;
        }        
    }

    for(int i = 0;i < numsSize; i ++){
        //printf("\n %d -- %d -- %dkkk",i, leftMin[i],rightMin[i]);
        if (leftMin[i] >= 0 && rightMin[i] < numsSize) {
            //printf("\n %d -hhh- %d -- %dkkk",i, totalSum - sumleft[leftMin[i]] - sumRight[rightMin[i]],rightMin[i]);
            long temp = (totalSum - sumleft[leftMin[i]] - sumRight[rightMin[i]])* *(nums + i);
            if (temp > result) {
                result = temp;
            }
        } else {
            if (leftMin[i] == -1 && rightMin[i] != numsSize) {
                long temp = (totalSum - sumRight[rightMin[i]])* *(nums + i);
                if (temp > result) {
                    result = temp;
                }
            } else if (leftMin[i] != -1 && rightMin[i] == numsSize) {
                    long temp = (totalSum - sumleft[leftMin[i]])* *(nums + i);
                    if (temp > result) {
                        result = temp;
                    }
            } else {
                long temp = (totalSum)* *(nums + i);
                    if (temp > result) {
                        result = temp;
                    }
            }
            
        }
    }

    return (result % ((int)pow(10,9) + 7)) ; 
}
//1,2,3,2
//0,1,2,2
//3,,2,3



bool IsEmpty(Stack S)
{
    return S->Next == NULL;
}

Stack  Pop(Stack S)
{
    PtrToNode FirstCell;
    FirstCell = S->Next;
    S->Next = S->Next->Next;
    return FirstCell;
}

void Push(long X, long index, Stack S)
{
    PtrToNode TmpCell;
    TmpCell = malloc(sizeof(struct Node));
    TmpCell->Element = X;
    TmpCell->index = index;
    TmpCell->Next = S->Next;
    S->Next = TmpCell;
}

Stack CreateStack(void)
{
    Stack S;
    S = malloc(sizeof(struct Node));
    S->Next = NULL;
   
    while(!IsEmpty(S))
        Pop(S);
    return S;
}

