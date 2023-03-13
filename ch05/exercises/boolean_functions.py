# def foo(param1,param2):
#     return param1+param2


# def bar(param1=4,param2=3):
#     return param1 + param2


# x=bar(2,4)
# print(x)

# def func():
#     pass

# def is_passing(letter):
#     return letter.lower() in "abc"

#print(is_passing("b"))


#accumalator a loop thats summing values
# result=0

# for i in range(10):
#     result=result+1

# print(result)
    

def remove_vowels(string):
    vowels="aeiou"
    vowels += vowels.upper()
    result=""
    for ch in string:
        if ch not in vowels:
            result+=ch
    return result

def main():
    mystring="Hello World"
    mystring=remove_vowels(mystring)
    print(mystring)