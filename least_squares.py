from matrix import Matrix

def tabular_function (n):
    tab_func = {}

    # Dictionary: key {x} --> value {f(x)} 
    for i in range(n):
        input_str = input("Input x and f(x) separated by a space (i = {}): ".format(i))
        x, y = input_str.split()
        x = float(x)
        y = float(y)
        tab_func[x] = y
    
    return tab_func

def least_squares (tab_func, x):
    x_val = list(tab_func.keys())
    y_val = list(tab_func.values())
    n = len(x_val)

    avg_x = 0
    avg_y = 0

    for i in range (n):
        avg_x += x_val[i]
        avg_y += y_val[i]
    else:
        avg_x /= n
        avg_y /= n

    sum_xy_diff = 0
    sum_xx_diff = 0

    for i in range(n):
        sum_xy_diff += (x_val[i] - avg_x) * (y_val[i] - avg_y)
        sum_xx_diff += (x_val[i] - avg_x) ** 2

    m = sum_xy_diff / sum_xx_diff
    b = avg_y - (m * avg_x)

    return (m * x) + b

def main ():
    n = int(input("Input the number of points: "))
    
    tab_func = tabular_function(n)

    x = float(input("\nInput the x value to aproximate: "))

    result = least_squares(tab_func, x)

    print("\nf(x) ≈ {:.5f} at x = {} \n".format(result, x))

main ()