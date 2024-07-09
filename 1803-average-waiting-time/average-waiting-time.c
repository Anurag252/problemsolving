double averageWaitingTime(int** customers, int customersSize, int* customersColSize) {

    if (customersSize == 0){
        return 0;
    }
    long wait = 0;
    int freeat = customers[0][0];
    for (int i = 0 ; i < customersSize ; i ++) {
        //printf("%d %d\n", freeat, wait);
        int diff = customers[i][1];
        if (freeat > customers[i][0]) {
            wait = wait + freeat - customers[i][0] + diff;  
        } else {
            // wait time is 
            freeat = customers[i][0];
            wait = wait + diff;
        }
        freeat = freeat + customers[i][1];
    }

    return ((double)(wait))/customersSize;
}