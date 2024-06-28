def tabular_function (n, h):
    tab_func = {}
    x = h

    # Dictionary: key {x} --> value {f(x)} 
    for i in range(n):
        y = float(input("f({}) = ".format(x)))
        tab_func[x] = y
        x += h

    return tab_func

def lagrange_polynomial (tab_func, x):
    x_values = list(tab_func.keys())
    y_values = list(tab_func.values())
    
    def L(x):
        n = len(x_values)
        result = 0.0
        
        for j in range(n):
            lagrangian = y_values[j]
            for m in range(n):
                if m != j:
                    lagrangian *= (x - x_values[m]) / (x_values[j] - x_values[m])
            result += lagrangian
        return result

    return L
    

n = int(input("Input the number of points: "))
h = float(input("Input the step size h: "))

tab_func = tabular_function(n, h)

x = float(input("\nInput the starting value of x: "))

L = lagrange_polynomial(tab_func, x)
L_eval = L(x)

print("f({}) ≈ {:.6f}".format(x, L_eval))
