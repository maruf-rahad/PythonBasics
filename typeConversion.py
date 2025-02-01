
birth_year = input("Enter birth year: ")
current_age = 2025 - int(birth_year)
print("Current age ", current_age)

first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

# concatenated the two numbers like 10 + 20 = 1020
result = first_number + second_number
print("result = " + result)
# after conversion like 10 + 10 = 20
result = (int(first_number) + int(second_number))
print("result = " + str(result))

first_number, second_number = map(float, input("Enter two float numbers: ").split())
result = first_number + second_number
print("result = " + str(result))
