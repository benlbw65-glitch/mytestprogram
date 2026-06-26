import math

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

def log(x, base=math.e):
    """Returns the logarithm of x to the given base (default natural log)."""
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers.")
    return math.log(x, base)

if __name__ == "__main__":
    print("Welcome to the simple test calculator program!")
    print(f"Running add(2, 3): {add(2, 3)}")
    print(f"Running subtract(5, 2): {subtract(5, 2)}")
    print(f"Running log(100, 10): {log(100, 10)}")

