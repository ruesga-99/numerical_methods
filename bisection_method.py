from math import log, ceil

def iterations_number (a, b, e):
    n = ceil((log(b-a) - log(e)) / log(2))
    return n


def calculate_middle_point (a, b):
    return (a + b) / 2

def evaluate_function (f, x):
    eval = 0.0
    n = len(f)

    for i in range(n):
        eval += (x ** i) * f[n - 1 - i]

    return eval

def bisection_method (n, a, b, f, epsilon):
    c = calculate_middle_point(a, b)

    print("\n i |     a     |     b     |     c     |     f(a)    |     f(b)    |     f(c)    ")

    for i in range(n):
        fa = evaluate_function(f, a)
        fb = evaluate_function(f, b)
        fc = evaluate_function(f, c)

        print("{:2d} | {:9.6f} | {:9.6f} | {:9.6f} | {:11.6f} | {:11.6f} | {:11.6f}".format(i, a, b, c, fa, fb, fc))

        if fa * fc < 0:
            # The solution exists within a and c
            b = c
            c = calculate_middle_point(a, b)
        elif fb * fc < 0:
            # The solution exists within c and b
            a = c
            c = calculate_middle_point(a, b)
        elif abs(fc) < epsilon:
            break
        else:
            print("The solution does not exist within the given interval")
            break

    print("\nThe solution is aproximately = {:9.6f}".format(c))

def main ():
    x = degree = int(input("Input the polinomial's degree: "))

    f = []
    while x > -1:
        f.append(float(input("Input the coefficient of x^{}: ".format(x))))
        x -= 1

    epsilon = float(input("Input the desired epsilon round error: "))

    a = float(input("Input a: "))
    b = float(input("Input b: "))

    n = iterations_number(a, b, epsilon)

    bisection_method(n, a, b, f, epsilon)

main()
