# try:
#     number_1 = int(input("number 1: "))
#     number_2 = int(input("number 2: "))

#     divide=number_1/number_2
#     print(divide)
# except ValueError as e:
#     print("Invalid Number",e)

# except ZeroDivisionError as e:
#     print("Division by zero not possible",e)




try:
    password = input("password: ")
   
    if len(password)<8:
        raise ValueError("weak password")

    print(password)

    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain a number")

except ValueError as e:
    print(e)

# or
# password = input("Enter password: ")
# try:
#     if len(password) < 8:
#         raise ValueError("Password too short")
#     print("Strong Password")
# except ValueError as e:
#     print(e)