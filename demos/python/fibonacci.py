#!/usr/bin/env python3
"""
Fibonacci Sequence Demonstration
--------------------------------
This script demonstrates different methods to calculate Fibonacci numbers.
"""

import time
import functools


def fibonacci_recursive(n):
    """Calculate the nth Fibonacci number using simple recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


@functools.lru_cache(maxsize=None)
def fibonacci_memoized(n):
    """Calculate the nth Fibonacci number using memoized recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_memoized(n-1) + fibonacci_memoized(n-2)


def fibonacci_iterative(n):
    """Calculate the nth Fibonacci number using iteration."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b


def benchmark(func, n, name):
    """Benchmark a function's execution time."""
    start = time.time()
    result = func(n)
    end = time.time()
    print(f"{name} result for n={n}: {result}")
    print(f"{name} time: {end - start:.6f} seconds")
    print("-" * 40)


def main():
    """Main function to demonstrate Fibonacci calculations."""
    print("Fibonacci Sequence Demonstration")
    print("=" * 40)
    
    # Test small values with all methods
    n_small = 20
    print(f"\nCalculating Fibonacci({n_small}) with different methods:")
    benchmark(fibonacci_iterative, n_small, "Iterative")
    benchmark(fibonacci_memoized, n_small, "Memoized recursive")
    benchmark(fibonacci_recursive, n_small, "Simple recursive")
    
    # Test larger value with efficient methods only
    n_large = 35
    print(f"\nCalculating Fibonacci({n_large}) with efficient methods:")
    benchmark(fibonacci_iterative, n_large, "Iterative")
    benchmark(fibonacci_memoized, n_large, "Memoized recursive")
    
    # Print first 10 Fibonacci numbers
    print("\nFirst 10 Fibonacci numbers:")
    for i in range(10):
        print(f"F({i}) = {fibonacci_iterative(i)}")


if __name__ == "__main__":
    main() 