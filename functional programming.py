def is_even(n):
    return n % 2 == 0

def multiply_by_2(n):
    return n * 2

def map_and_filter(numbers):
    return list(map(multiply_by_2, filter(is_even, numbers)))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = map_and_filter(numbers)
print(result) 
