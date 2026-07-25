# my_str ="poom"
# def palindrome(s):
#     string=s.lower().replace(" ","")
#     if string == string[::-1]:
#         print("The string is a palindrome.")
#     else:
#         print("The string is not a palindrome.")
# palindrome(my_str)


# my_list = [5,66,45,3,6,7]
# def second_largest(lst):
#     max_of_list=max(lst)
#     lst.remove(max_of_list)
#     second_max=max(lst)
#     return second_max
# second_largest_num = second_largest(my_list)
# print(second_largest_num)


# students = [
#     {"name":"dada","age":50},
#     {"name":"pota","age":22},
#     {"name":"bapa","age":30}
# ]
# students.sort(key=lambda x: x["age"])
# print(students)


# santance = "The quick brown fox jumps over the lazy dog. the red fox is quick and smart."
# def word_count(santance):
#     word_list = santance.lower().replace(".","").split(" ")
#     count_list= {word: word_list.count(word) for word in word_list}
#     print(count_list)
#     maximum = max(count_list.items())
# word_count(santance)