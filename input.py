# input method will return a value that we enter into the terminal

# input a string
name = input("What is your name? ")
print("Hello "+ name)
# integer
age = input("How old are you? ")
print(age)
# double
money = input("How much money do you have? ")
print(money)

# input
a, b, c = map(int, input("Enter 3 numbers ").split())
print("a = ", a, " b = ", b, " c = ", c)
print("a = " + str(a) + " b = " +  str(b) + " c = " + str(c))


# input as list separated by space in a single line
numbers = list(map(int, input("Enter numbers ").split()))
print("numbers ", numbers)

# input as list separated by comma in a single line
numbers = list(map(int, input("Enter numbers ").split(",")))
print("numbers ", numbers)