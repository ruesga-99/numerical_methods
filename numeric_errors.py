def absolute_error (value, aproximate):
    return abs(value - aproximate)

def relative_error (value, aproximate):
    return abs(absolute_error(value, aproximate)/ abs(value))

def percentage_error (value, aproximate):
    return relative_error(value, aproximate) * 100

def mean_absolute_error (values, aproximates):
    n = len(values)
    mae = 0.0
    for i in range (n):
        mae += absolute_error(values[i], aproximates[i])
    mae /= n

    return mae

def mean_squared_error (values, aproximates):
    n = len(values)
    mse = 0.0
    for i in range (n):
        mse += absolute_error(values[i], aproximates[i]) ** 2
    mse /= n

    return mse

def root_mean_squared_error (values, aproximates):
    return (mean_squared_error(values, aproximates)) ** 0.5

# Example usage
values = [10, 20, 30, 40, 50]
aproximates = [11, 19, 31, 42, 48]

print("Absolute Error: ", absolute_error(values[0], aproximates[0]))
print("Relative Error: ", relative_error(values[0], aproximates[0]))
print("Percentage Error: ", percentage_error(values[0], aproximates[0]), "%")
print("Mean Absolute Error: ", mean_absolute_error(values, aproximates))
print("Mean Squared Error: ", mean_squared_error(values, aproximates))
print("Root Mean Sauared Error: ", root_mean_squared_error(values, aproximates))