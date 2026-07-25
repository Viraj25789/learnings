user_pass="Vir@j123"
input_pass=str(input("Enter your password: "))

if input_pass=="":
    print("ENTER VALID PASSWORD!")

elif input_pass==user_pass:
    print("LOGIN SUCCESSFULLY! ")

else:
    print("INVALID PASSWORD!")




marks = 101



if marks < 35:
    print("FAIL")

elif marks < 60:
    print("pass")

elif marks < 80:
    print("good")

elif marks < 100:
    print("excellent")

else:
    print("fail")