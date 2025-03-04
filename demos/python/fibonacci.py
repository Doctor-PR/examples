import sys

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def main():
    if len(sys.argv) != 2:
        print("Usage: python fibonacci.py <n>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        if n < 0:
            print("Please provide a non-negative integer")
            sys.exit(1)
        print(f"Fibonacci({n}) = {fibonacci_recursive(n)}")
    except ValueError:
        print("Please provide a valid integer")
        sys.exit(1)


if __name__ == "__main__":
    main()
