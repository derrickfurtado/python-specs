import oneone

print("top level in 2.py")

oneone.func()

if __name__ == "__main__":
    print("LOGIC ============ 2.py is being run directly")
else:
    print('LOGIC ============== 1.py is being imported')


print("1.py is: ", oneone.__name__)
print("2.py is: ", __name__)
