int replace(int numBottles, int numExchange, int emptyBottle) {
    
    printf("%d %d %d\n", numBottles, numExchange ,emptyBottle);
    if (emptyBottle >= numExchange) {
        numBottles += emptyBottle / numExchange;
        emptyBottle = emptyBottle % numExchange;
    }

    if (numBottles  == 0) {
        return 0;
    }

    return numBottles +   replace(numBottles/numExchange  , numExchange, emptyBottle + (numBottles % numExchange) );
}

int numWaterBottles(int numBottles, int numExchange) {
    return replace(numBottles, numExchange, 0);
}