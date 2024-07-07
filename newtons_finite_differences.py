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

def forward_finite_differences (tab_func, x):
    x_val = list(tab_func.keys())
    y_val = list(tab_func.values())
    n = len(x_val)

    h = y_val[1] - y_val[0]
    s = (x - x_val[0]) / h

    table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        table[i][0] = y_val[i]

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]

    return table, x_val, True

def backward_finite_differences (tab_func, x):
    x_val = list(tab_func.keys())
    y_val = list(tab_func.values())
    n = len(x_val)

    h = y_val[1] - y_val[0]
    s = (x - x_val[0]) / h

    table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        table[i][0] = y_val[i]

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1])

    return table, x_val, False

def print_table(table, x_val, type):
    n = len(x_val)
    
    # Table header
    headers = ["i", "xi", "f(xi)", "|"]

    # Type: True = Forward --- False = Backward
    if type == True:
        headers += ["Δ^{}f(x)".format(i+1) for i in range(n-1)]
    else:
        headers += ["∇^{}f(x)".format(i+1) for i in range(n-1)]
    
    print("\t".join(headers))

    # Table rows
    for i in range(n):
        row = [f"{i}", f"{x_val[i]:.3f}", f"{table[i][0]:.3f}", "|"]
        for j in range(1, n):
            if i < n - j:
                row.append(f"{table[i][j]:.3f}")
            else:
                row.append("")
        print("\t".join(row))

def main ():
    n = int(input("Input the number of points: "))
    
    tab_func = tabular_function(n)

    x = float(input("\nInput the x value to interpolate: "))

    table, x_val, type = forward_finite_differences(tab_func, x)

    print("\n\033[1mForward Finite Differences\033[0m \n")
    print_table(table, x_val, type)

    table, x_val, type = backward_finite_differences(tab_func, x)

    print("\n\033[1mBackward Finite Differences\033[0m \n")
    print_table(table, x_val, type)
    
    return

main ()