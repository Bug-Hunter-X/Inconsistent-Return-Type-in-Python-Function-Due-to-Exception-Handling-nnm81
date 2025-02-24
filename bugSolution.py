def function_with_consistent_return_type(x):
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return 0 #or raise an exception instead

#The improved version consistently returns a float or an integer(0 in this case). This makes the function behavior predictable.

# Example usage:
result1 = function_with_consistent_return_type(2)
print(f"Result 1: {result1}")  # Output: Result 1: 5.0

result2 = function_with_consistent_return_type(0)
print(f"Result 2: {result2}")  # Output: Error: Cannot divide by zero.
                                # Result 2: 0