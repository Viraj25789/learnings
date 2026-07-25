# list=[i**3 for i in range(1,6)]
# print(list)

# santance="hello i am viraj"
# matching=[char for char in santance if char in "aei"]
# matching = set(matching)
# matching=[i for i in matching]
# print(matching)

def countdown(n):

    for i in range(n, 0,-1):
        yield i
    
for num in countdown(5):
    print(num)