int countSeniors(char ** details, int detailsSize){
    int result = 0;

    for (int i = 0 ; i < detailsSize ; i ++) {
        
        if ( (details[i][11] - '0') * 10 + (details[i][12] - '0') > 60) {
            result ++;
        }
    }
    return result;

}