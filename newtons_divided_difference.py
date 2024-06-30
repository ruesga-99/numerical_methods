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

def divided_difference (tab_func, n):
    x_val = list(tab_func.keys())
    y_val = list(tab_func.values())

    dev_1 = []
    dev_2 = []
    dev_3 = []
            
    for i in range(n - 1):
        dev_1.append((y_val[i + 1] - y_val[i]) / (x_val[i + 1] - x_val[i]))

    for i in range(n - 2):
        dev_2.append((dev_1[i + 1] - dev_1[i]) / (x_val[i + 2] - x_val[i]))

    for i in range(n - 3):
        dev_3.append((dev_2[i + 1] - dev_2[i]) / (x_val[i + 3] - x_val[i]))

n = int(input("Input the number of points: "))

tab_func = tabular_function(n)

divided_difference(tab_func, n)
