def even_parameters(func):
    def wrapper(*args):
        if all(isinstance(x, int)and x%2 == 0 for x in args):
            result = func(*args)
            return result
        else:
            return f"Please use only even numbers!"
    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))