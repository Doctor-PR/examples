import argparse

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def main():
    parser = argparse.ArgumentParser(description='Calculate the nth Fibonacci number.')
    parser.add_argument('n', type=int, help='The position in the Fibonacci sequence')
    args = parser.parse_args()
    
    result = fibonacci_recursive(args.n)
    print(f"Fibonacci({args.n}) = {result}")


if __name__ == "__main__":
    main()
