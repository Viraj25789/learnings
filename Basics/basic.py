num_1= 12
num_2 = 5
str1= "viraj"
str2= "kumar"
float_1= 12.5
float_2= 5.5
bool1= True
bool2= False

# print(bool1 + str1)


print(type(str1))
print(type(float_1))
print(type(bool1))

print(id(str1))
print(id(num_1))
print(id(num_2))
print(id(float_1))
print(id(bool1))


list_1= [1,2,3,4,5]
print(type(list_1))
print(id(list_1))
print(list_1)

list_2 = list_1
list_2.append(6)

print(list_1)
print(list_2)

print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)    
print(num_1 / num_2)
print(num_1 // num_2)
print(num_1 % num_2)
print(num_1 ** num_2)
print(num_1 > num_2)

print('heloo', "world", sep= "--")

print('heloo', end=" ")
print("world")