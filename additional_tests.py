# Additional tests for the recursive functions in Practical-4.

def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def recursive_search(items, target, index=0):
    if index >= len(items):
        return -1
    if items[index] == target:
        return index
    return recursive_search(items, target, index + 1)


# factorial tests
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(9) == 362880

try:
    factorial(-1)
    raise AssertionError("factorial(-1) should raise ValueError")
except ValueError:
    pass

# recursive_search tests
assert recursive_search([8, 3, 12, 7], 12) == 2
assert recursive_search([8, 3, 12, 7], 5) == -1
assert recursive_search([8, 3, 12], 8) == 0
assert recursive_search([], 1) == -1

print("All additional tests passed.")
