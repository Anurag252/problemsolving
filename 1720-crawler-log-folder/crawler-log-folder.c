int minOperations(char** logs, int logsSize) {

    int level = 0;
    for (int i = 0 ; i < logsSize; i ++) {
        if (strcmp(logs[i] , "../" ) == 0) {
            level  = (level == 0 ? 0 : level - 1) ;
            continue;
        }

        if (strcmp(logs[i] , "./" ) == 0) {
            
            continue;
        }


        level ++ ;


    }
    return level ;
}