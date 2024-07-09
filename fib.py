def fib(n):
    """
    Calculate the nth Fibonacci number.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def generate_fibonacci(n):
    """
    Generate a list of the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        list: A list of the first n Fibonacci numbers.
    """
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_nth(n):
    """
    Calculate the nth Fibonacci number using an efficient algorithm.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <n>")
        sys.exit(1)

    n = int(sys.argv[1])
    result = fib(n)
    print(f"The {n}th Fibonacci number is: {result}")

if __name__ == "__main__":
    main()
