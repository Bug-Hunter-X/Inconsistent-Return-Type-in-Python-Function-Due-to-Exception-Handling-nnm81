def function_with_uncommon_error(x):
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

# The uncommon error is a subtle one where the return type can change depending on the input.
# If x is not zero, it returns a float. If x is zero, it returns None.
# This can lead to unexpected behavior in other parts of the program if the caller is not aware of this.

# Example usage:
result1 = function_with_uncommon_error(2)
print(f"Result 1: {result1}")  # Output: Result 1: 5.0

result2 = function_with_uncommon_error(0)
print(f"Result 2: {result2}")  # Output: Error: Cannot divide by zero.
                                # Result 2: None