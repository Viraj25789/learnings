name="viraj"
surname="parmar"

user_name = name
user_name = user_name.replace("v", "rutu")

# print(name)
# print(user_name)

full_name= name + " " + surname

# print(full_name)
# print(full_name.title())
# print(full_name.strip())
# print(full_name.replace(" ",""))


newname= full_name.split(" ")

print(newname[1],'',newname[0])
# or
first, second= newname[1], newname[0]
print(first, second)