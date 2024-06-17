bool judgeSquareSum(int c) {
    if (c == 0) {
        return true;
    }
    for (int i = 1 ; i <= (int)(sqrt(c)) ; i ++) {
        double k = sqrt(c- i*i);
        if ((int)(k) == k) {
            //printf(" %d %d\n",k, i);
            return true;
        }
    }
    return false;
    
}