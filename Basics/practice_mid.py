# def count_vovels(s):
#     s = s.replace(' ','')
#     print(s)
#     vovels= ["a","e","i","o","u"]
#     result = [s.count(i) for i in vovels]
#     print(result)
#     return sum(result)
# strings ="hello my name is viraj"
# print(count_vovels(strings))



# string ="pooja"
# def reverse(s):
#     t = list(s)
#     t.reverse()
#     ss = "".join(t)
#     return ss
# ss = reverse(string)
# print(ss)



# lst = [1,3,2,3,1,4]
# def sum_list(lst):
#     sum=[]
#     for i in lst:
#         sum.append(i)

#         if len(sum) == 1:
#             pass
#         elif len(sum) == 2:
#             do = sum[0]+sum[1]
#             sum.clear()
#             sum.append(do)
#     return sum

# result = sum_list(lst)
# print(result)




# def maxm(lst):
#     lst.sort()
#     return lst[len(lst)-1]

# lst = [1,3,9,2,5,6]

# print(maxm(lst))



# def celsius_to_fahrenheit(c):
#     f = (c * 9/5) + 32
#     return f

# print(celsius_to_fahrenheit(0))    # should print 32.0
# print(celsius_to_fahrenheit(100))  # should print 212.0


# num = [1,2,3,4]
# sqr = list(map(lambda x: x**2 ,num))
# print(sqr)

# fil = list(filter(lambda x: x>3 ,num))
# print(fil)

for i in range(1,6):
    for i in (1,i):
        print(""*i)
    print('*'*i)