import send2trash

# def func_needs_decorator():
#     print("String")

# def new_decorator(original_func):
    
#     def wrap_func():
#         print("before============")
#         original_func()
#         print("after==============")
#     return wrap_func

# # func_needs_decorator()


# decorated_func = new_decorator(func_needs_decorator)

# # decorated_func()



# # @new_decorator
# def func_needs_decorator():
#     print("String")


# func_needs_decorator()



# print("==================================================")

num = 5

def math_func(num):
    return num ** 2

def decorator(x):
    def wrapper(num):
        return x(num) +num
    return wrapper



print(f"Original function where {5} squared = ",math_func(num))

@decorator
def math_func(num):
    return num ** 2

print(f"Wrapped function where {num} squared + {num} = ",math_func(num))





print("==================================================")

cubes = 10
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print("This process takes a lot of memory 👇")
print("creating data in a list using range generator", create_cubes(cubes), "\n")

def create_eff_cubes(n):
    for x in range(n):
        yield x ** 3

print("This process LESS memory 👇")
print("creating data in a list using create cubes generator\n")

for x in create_eff_cubes(cubes):
    print(x)


print("\n\nFibonachi Sequence \n")

def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for number in gen_fibon(cubes):
    print(number)


print("\nSimple generator function: \n")
def simple_generator():
    for x in range(5):
        yield x

for numb in simple_generator():
    print(numb)

g = simple_generator()

print("\nUsing next() function\n")

print(next(g))  # = 0
print(next(g))  # = 1
print(next(g))  # = 2
print(next(g))  # = 3
print(next(g))  # = 4
# print(next(g))  # = ERROR because the generator only goes to range(5)


print("\nUsing iter() function\n")


s = "hello"

print(iter(s))      #cannot iterate over a string

s_iter = iter(s)    #must make it iterable first

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))


print("==================================================")

f = open("test.txt", "w+")
f.write("This is a test file creation")
f.close()




print("==================================================")

