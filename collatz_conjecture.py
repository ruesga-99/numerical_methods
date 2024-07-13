def collatz (n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
    
def main ():
    n = int(input("Input a positive integer: "))
    iterations = 0

    while n != 1:
        n = collatz(n)
        print(n)
        iterations += 1
    else:
        print("\nTotal iterations: {}".format(iterations))

main()