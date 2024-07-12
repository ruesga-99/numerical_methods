def evaluate_function (f, x, y):
    local_vars = {'x': x, 'y': y}
    return eval(f, {"__builtins__": None}, local_vars)

def runge_kutta (f, x0, xf, n):
    h = (xf - x0) / n

    xi = x0
    yi = float(input("Input initial value y0: "))

    print("\ni\t|xi\t\t|yi")

    i = 0
    while xi <= xf:
        print(f"{i}\t|{xi:.5f}\t|{yi:.5f}")

        k1 = evaluate_function(f, xi, yi)
        k2 = evaluate_function(f, xi+(h/2), yi+(h/2)*k1)
        k3 = evaluate_function(f, xi+(h/2), yi+(h/2)*k2)
        k4 = evaluate_function(f, xi+h, yi+h*k3)

        result = yi # Saved temporary to prevent additional itterations on the result
        yi = yi + (h/6) * (k1 + 2*k2 + 2*k3 +k4)
        xi += h
        i += 1

    return result

def main ():
    f = input("Input the function f(x,y): ")
    x0 = float(input("Input x0: "))
    xf = float(input("Input xf: "))
    n = int(input("Input the number of steps (n): "))

    yi = runge_kutta(f, x0, xf, n)

    print("\ny({}) ≈ {:.5f} \n".format(xf, yi))

main()