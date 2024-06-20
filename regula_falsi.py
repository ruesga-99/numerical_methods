from math import log, ceil

def calculate_c (a, b, f):
    fa = evaluate_function(f, a)
    fb = evaluate_function(f, b)
    c = ((a * fb) - (b * fa)) / (fb - fa)
    
    return c

def evaluate_function (f, x):
    eval = 0.0
    n = len(f)

    for i in range(n):
        eval += (x ** i) * f[n - 1 - i]

    return eval

def regula_falsi (a, b, f, epsilon):
    c = calculate_c(a, b, f)
    fc = evaluate_function(f, c)
    i = 0
    
    print("\n i |     a     |     b     |     c     |     f(a)    |     f(b)    |     f(c)    ")

    while abs(fc) >= epsilon:
        fa = evaluate_function(f, a)
        fb = evaluate_function(f, b)
        fc = evaluate_function(f, c)

        print("{:2d} | {:9.6f} | {:9.6f} | {:9.6f} | {:11.6f} | {:11.6f} | {:11.6f}".format(i, a, b, c, fa, fb, fc))

        if fa * fc < 0:
            # A solution exists within a and c
            b = c
            c = calculate_c(a, b, f)
        elif fb * fc < 0:
            # A solution exists within c and b
            a = c
            c = calculate_c(a, b, f)
        else:
            print("The solution does not exist within the given interval")
            break

        i += 1

    print("\nThe solution is aproximately = {:9.6f}".format(c))

def main ():
    x = int(input("Input the polinomial's degree: "))

    f = []
    while x > -1:
        f.append(float(input("Input the coefficient of x^{}: ".format(x))))
        x -= 1

    epsilon = float(input("Input the desired epsilon round error: "))

    a = float(input("Input a: "))
    b = float(input("Input b: "))

    regula_falsi(a, b, f, epsilon)

main()
