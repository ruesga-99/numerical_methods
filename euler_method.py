def evaluate_function (f, x, y):
    local_vars = {'x': x, 'y': y}
    return eval(f, {"__builtins__": None}, local_vars)

def euler_method (f, x0, xf, n):
    h = (xf - x0) / n

    xi = x0
    yi = float(input("Input initial value y0: "))

    print("\ni\t|xi\t\t|yi")

    i = 0
    while xi <= xf:
        print(f"{i}\t|{xi:.5f}\t|{yi:.5f}")
        yi = yi + h * evaluate_function(f, xi, yi)
        xi += h
        i += 1

    return yi

def main ():
    f = input("Input the function f(x,y): ")
    x0 = float(input("Input x0: "))
    xf = float(input("Input xf: "))
    n = int(input("Input the number of steps (n): "))

    yi = euler_method(f, x0, xf, n)

    print("\ny({}) ≈ {:.5f} \n".format(xf, yi))

main()