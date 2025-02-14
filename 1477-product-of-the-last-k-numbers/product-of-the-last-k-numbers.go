import "math/big"

type ProductOfNumbers struct {
    arr []*big.Int
    curr *big.Int
    mp map[int]bool
}


func Constructor() ProductOfNumbers {
    return ProductOfNumbers{
        arr : make([]*big.Int, 0),
        curr : big.NewInt(1),
        mp : make(map[int]bool),
    }
}

func Mul(x, y *big.Int) *big.Int {
    return big.NewInt(0).Mul(x, y)
}


func Div(x, y *big.Int) *big.Int {
    return big.NewInt(0).Div(x, y)
}

func (this *ProductOfNumbers) Add(num int)  {
    if num == 0 {
        this.mp[len(this.arr)] = true // inc by 1
        num = 1
    }

    this.curr = Mul(this.curr, big.NewInt(int64(num)))
    this.arr = append(this.arr, this.curr)
}


func (this *ProductOfNumbers) GetProduct(k int) int {
    //fmt.Println(this.arr, k, this.mp)

    for i := range k {

        t := len(this.arr) - 1 - i
        _, ok := this.mp[t]
        if ok {
            return 0
        }
    }

    if len(this.arr)-1-k >= 0 {
        t := Div(this.arr[len(this.arr)-1] , this.arr[len(this.arr)-1-k])
        return int(t.Int64())
    } else {
         return int(this.arr[len(this.arr)-1].Int64())
    }
     // assume list has k numbers
   
    
}


/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(num);
 * param_2 := obj.GetProduct(k);
 */