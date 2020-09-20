#include <stdio.h>
#include <math.h>
#include <conio.h>

double f(double y){
}

double y_check(double x){
}

int main(){
    double a;
    double b;
    double h;
    int n;
    a = 0; b = 2;
    h = 0.001;
    n = ceil((((b-a)/h + 1)));
    double x[n];
    double y[n];
    double u[n];
    y[0] = 1;
    u[0] = 2;
    for (int i = 0; i<n-1; i++){
        x[i+1] = x[i] + h;
        y[i+1] = y[i] + h*u[i];
        u[i+1] = u[i] + h*f(y[i]);
        printf("%f | %f | %f\n", x[i+1], y[i+1], y_check(x[i+1]));
    }
    _getch();
    return 0;
}