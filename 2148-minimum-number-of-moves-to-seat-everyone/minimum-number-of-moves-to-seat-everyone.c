int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int minMovesToSeat(int* seats, int seatsSize, int* students, int studentsSize) {
    qsort(seats, seatsSize, sizeof(int), cmpfunc);
     qsort(students, studentsSize, sizeof(int), cmpfunc);
    int result = 0;
     for (int i = 0 ; i < seatsSize ; i ++){
        if (seats[i] - students[i] > 0) {
            result += seats[i] - students[i];
        } else {
            result +=  students[i] - seats[i] ;
        }
        
     }
     return result;
}