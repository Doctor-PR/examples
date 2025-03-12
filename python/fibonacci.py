import argparse


def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def main():
    parser = argparse.ArgumentParser(description="Calculate the nth Fibonacci number.")
    parser.add_argument("n", type=int, help="The position in the Fibonacci sequence")
    parser.add_argument("--method", "-m", choices=["recursive", "iterative"], 
                        default="iterative", help="Method to calculate Fibonacci (default: iterative)")
    args = parser.parse_args()

    if args.method == "recursive":
        result = fibonacci_recursive(args.n)
    else:
        result = fibonacci_iterative(args.n)
        
    print(f"Fibonacci({args.n}) = {result}")


if __name__ == "__main__":
    main()
