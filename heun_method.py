def evaluate_function (f, x, y):
    local_vars = {'x': x, 'y': y}
    return eval(f, {"__builtins__": None}, local_vars)

def heun_method (f, x0, xf, n):
    h = (xf - x0) / n

    xi = x0
    yi = float(input("Input initial value y0: "))

    print("\ni\t|xi\t\t|yi")

    i = 0
    while xi <= xf:
        print(f"{i}\t|{xi:.5f}\t|{yi:.5f}")
        y_transient = yi + h * evaluate_function(f, xi, yi)
        result = yi # Saved temporary to prevent additional itterations on the result
        yi = yi + (h/2) * (evaluate_function(f, xi, yi) + evaluate_function(f, xi+h, y_transient))
        xi += h
        i += 1

    return result

def main ():
    f = input("Input the function f(x,y): ")
    x0 = float(input("Input x0: "))
    xf = float(input("Input xf: "))
    n = int(input("Input the number of steps (n): "))

    yi = heun_method(f, x0, xf, n)

    print("\ny({}) ≈ {:.5f} \n".format(xf, yi))

main()