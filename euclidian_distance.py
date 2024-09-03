def point_sets (n):
    point_set = {}

    # Dictionary: key {x} --> value {f(x)} 
    for i in range(n):
        input_str = input("Input x and f(x) separated by a space (i = {}): ".format(i))
        x, y = input_str.split()
        x = float(x)
        y = float(y)
        point_set[x] = y
    
    return point_set

def euclidean_distance (x1, y1, x2, y2):
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** .5

def main():
    n = int(input("Enter the number of known points: "))
    
    point_set = point_sets(n)
    print("")

    distances = []

    # Nested loop to calculate and print the distance between all pairs of points
    for x1 in point_set:
        for x2 in point_set:
            if x1 == x2:    #
                continue
            y1 = point_set[x1]
            y2 = point_set[x2]
            distance = euclidean_distance(x1, y1, x2, y2)
            distances.append(distance)
            print(f"Distance between ({x1}, {y1}) and ({x2}, {y2}): {distance}")
        print("")

    # Show the shortest distance
    print(f"The minimal distance between the given points is: {max(distances)}")

main()