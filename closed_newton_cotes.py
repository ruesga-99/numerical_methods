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
    x_values = sorted(tab_func.keys())
    h = (x_values[-1] - x_values[0]) / (len(x_values) - 1)

    return h

    return h

def trapezium_method (tab_func, h):
    x_values = sorted(tab_func.keys())

    n = len(x_values)
    integral = 0.5 * (tab_func[x_values[0]] + tab_func[x_values[-1]])
    
    for i in range(1, n - 1):
        integral += tab_func[x_values[i]]
    
    integral *= h
    return integral

def simpson_1_3 (tab_func, h):
    x_values = sorted(tab_func.keys())

    n = len(x_values)
    integral = tab_func[x_values[0]] + tab_func[x_values[-1]]
    
    for i in range(1, n - 1):
        if i % 2 == 0:
            integral += 2 * tab_func[x_values[i]]
        else:
            integral += 4 * tab_func[x_values[i]]
    
    integral *= h / 3
    return integral 

def main ():
    n = int(input("Enter the number of known points: "))
    
    tab_func = tabular_function(n)
    h = calculate_step(n, tab_func)

    if n == 1:
        result = trapezium_method(tab_func, h)
    elif n == 2:
        result = simpson_1_3(tab_func, h)

    print("\nThe approximate integral is: {:.5f} \n".format(result))

main()