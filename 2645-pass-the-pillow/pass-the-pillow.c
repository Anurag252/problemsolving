int passThePillow(int n, int time) {


    if (((time / (n-1)) % 2) == 1) {
        // returning
        return n-(time % (n-1));
        
    } else {
        return (time % (n-1)) + 1;
        // going forward
    }
}

// 2