/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func modifiedList(nums []int, head *ListNode) *ListNode {
    var prev *ListNode = nil
    sort.Ints(nums)
    temp := head
    for temp != nil {
        //found := false
        if binSearch(nums, temp.Val) {
                    if (prev == nil) {
                        //fmt.Println(temp.Val, head.Val, "B")
                        temp = temp.Next
                        head = head.Next

                    } else {
                        //fmt.Println(temp.Val, head.Val, "A")
                        prev.Next = temp.Next
                        temp = temp.Next
                    }
                } else {
                     prev = temp
                    temp = temp.Next
                }
            }
            
    
    return head
}
func binSearch(arr []int, val int) bool {
    start := 0
    end := len(arr)-1

    for start <= end {
        mid := (start + end)/2
        if (arr[mid] < val){
            start = mid + 1
            continue
        }

        if (arr[mid] > val){
            end = mid - 1
            continue
        }

        if (arr[mid] == val){
           return true
        }
    }
    //fmt.Println(arr, val)
    return false
}
