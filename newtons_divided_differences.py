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

def divided_differences (tab_func):
    x_val = list(tab_func.keys())
    y_val = list(tab_func.values())
    n = len(x_val)

    table = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        table[i][0] = y_val[i]
    
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x_val[i + j] - x_val[i])
    
    return table, x_val

def interpolate(table, x_val, x):
    n = len(x_val)
    result = table[0][0]
    product_terms = 1.0
    
    for i in range(1, n):
        product_terms *= (x - x_val[i - 1])
        result += table[0][i] * product_terms
    
    return result

def print_table(table, x_val):
    n = len(x_val)
    
    # Table header
    headers = ["i", "x", "f(x)", "|"]
    headers += ["y^{}".format(i+1) for i in range(n-1)]
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

def main():
    n = int(input("Input the number of points: "))
    
    tab_func = tabular_function(n)
    table, x_val = divided_differences(tab_func)

    print_table(table, x_val)
    
    x = float(input("\nInput the x value to interpolate: "))
    polynomial_aprox = interpolate(table, x_val, x)
    
    print("\nf(x) ≈ {} at x = {} \n".format(polynomial_aprox, x))

main()