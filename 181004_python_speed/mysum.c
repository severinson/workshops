# include <stdio.h>

/* return the sum of the elements of data
 */
double mysum(double data[], int m) {
    double result = 0;
    for (int i = 0; i < m; i++) {
        result += data[i];
    }
    return result;
}

int main() {
    int m = 100000;
    int n = 10000;

    // create an array of floats from 0 to m
    double data[m];
    for (int i = 0; i < m; i++) {
        data[i] = (double) i;
    }

    // compute the sum of the array n times
    double result = 0;
    for (int i = 0; i < n; i++) {
        result += mysum(data, m);
    }

    // print summary and exit
    result /= m * n;
    printf("computed the sum %d floats %d times. normalized result=%f\n",
           m, n, result);
    return 0;
}
