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

def calculate_step (n, tab_func):
    x_values = tab_func.keys()

    h = (x_values[-1] - x_values[0]) / n

    return h

def trapezium_method (tab_func, h):
    x_values = tab_func.keys()
    y_values = tab_func.values()

    return 

def main ():
    n = int(input("Enter the number of known points: "))
    
    tab_func = tabular_function(n)

    h = calculate_step(n, tab_func)


main()