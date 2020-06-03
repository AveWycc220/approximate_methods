import ast

def gauss_seidel(a, x , b):
    xtemp = [0 for i in range(N)]
    while True:
        maxe = 0
        for j in range(N):
            xtemp
            d = b[j]
            for i in range(N):
                if(j != i):
                    d-=a[j][i] * x[i]
            x[j] = d / a[j][j]
            if (abs(xtemp[j] - x[j]) > maxe):
                maxe = abs(xtemp[j] - x[j])
            xtemp[j] = x[j]
        if (maxe < EPS):
            break
    return x

if __name__ == "__main__":
    try: 
        EPS = ast.literal_eval(input("Input accuracy\n"))
        N = ast.literal_eval(input("Input size of square matrix\n"))
        x = [0 for i in range(N)]
        a = ast.literal_eval(input("Input matrix like '[[a11, a12, a13 ... a1N][a21, a22, a23 ... a2N] ...\
[aN1, aN2, aN3 ... aNN]]'\n"))
        b = ast.literal_eval(input("Input result of equation like [b1, b2, b3 ... bN]\n"))
        if (isinstance(a,list) and isinstance(b, list) and isinstance(N, int) and len(a) == N and len(b) == N):
            x = gauss_seidel(a, x, b)
            print(x)
        else:
            print("Wrong input")
    except ValueError:
        print("Wrong input")