def my_basket(*args,**kwargs):
    if 'fruit' in kwargs:
        print(f"My basket contains {kwargs['fruit']} fruits.")
    elif 'veggie' in kwargs:
        print(f"My basket contains {kwargs['veggie']} vegetables.")


my_basket(veggie="cucumber")


print("===================================")


def my_basket2(*args,**kwargs):
    print(args)
    print(kwargs)

my_basket2(30,40,10,fruit="orange", drinks="Monster Energy")

print("===================================")



def even_capitalized(string):
    new_string = ""
    string = string.replace(' ','')
    string = string.replace('.','')
    for x in range (0,len(string)):
        if x % 2 == 0:
            new_string = new_string + string[x].upper()
        else:
            new_string = new_string + string[x].lower()
        
    return new_string
        
even_capitalized("test string")
even_capitalized("This string will test this function further. It adds additional sentences too.")



print("===================================")

def third(num):
    return num * 3

my_nums = [1,2,3,4,5,6,7,8,9,10]

for x in map(third, my_nums):
    print(x)

func = list(map(third, my_nums))

print(func)



print("===================================")

def check_even(num):
    return num % 2 is not 0

for x in filter(check_even,func):
    print(x)

check = list(filter(check_even,func))
print(check)





print("===================================")


l = [1,2,3]
s = {1,2,3}
d = {"a":{1,2,3}, "b":2, "c":3},{"d":1, "e":2, "f":3}
t = (1,2,3)

print("this should be a list:", type(l))
print("this should be a set:", type(s))
print("this should be a dictionary:", type(d))
print("this should be a tuple:", type(t))