# print(type(__name__))

# __name__ = "__second__"

# print(__name__)

def func():
    print("Func() in 1.py")

print("Top level in 1.py")

if __name__ == '__main__':
    print('LOGIC =========== 1.py is being run directly')
else:
    print("LOGIC ============= 1.py has been imported")