print("======================")


myList = [1,2,3,4,5,6,7,8,9,10]

print("My list before: ", myList)


myList.insert(3,11)

print("My list after inserting 11 value into 3rd index: ", myList)

print("======================")

def hello():
    x = "hello"
    return x


print(hello())

print("======================")


def say_hello (name="default"):                 # add in this syntax to avoid errors and have a fallback variable
    print(f"Hey {name}!. How are you?")


say_hello("John")
say_hello()






print("======================")


def sum_num(num1, num2):
    print(num1+num2)
    return num1 + num2




# def sum_num(num1, num2):                      #fix function
#     num1 = int(num1)
#     num2 = int(num2)
#     print(num1+num2)
#     return num1 + num2


# return correctly with integers

sum_num(20,30)


# return as string
sum_num('20','30')





print("======================")



def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return
    return n



primeNumbers = []

def sort_prime_num(start, stop):
    for i in range(start,stop):
        if is_prime(i) is not None:
            primeNumbers.append(i)
        else:
            continue


# sort_prime_num(0, 100)
# sort_prime_num(100, 1000)
# sort_prime_num(1000, 10000)
# sort_prime_num(10000, 100000)

print("The number of primes is: ", len(primeNumbers))





print("======================")

crypto_prices = (("Bitcoin", 45000), ("Ether", 3300), ("XRP", 45))

for x, y in crypto_prices:
    print(x)
    
for x, y in crypto_prices:
    print(y)

def check_highest_price(tup):
    highest_price = 0
    highest_coin = 0
    for name, price in tup:
        if price > highest_price:
            highest_price = price
            highest_coin = name
        else:
            continue
    return (highest_coin, highest_price)
        

print("highest priced coin is: ", check_highest_price(crypto_prices))

print("======================")


n = int(input())


squared = []


for number in range(0,n):
    squared.append(number * number)

print(squared)



print("======================")




