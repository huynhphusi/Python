import random

mylist = ["apple", "banana", "cherry"]      # Cho trước một array
x = random.randint(0,len(mylist)-1)         # Random số nguyên: random.randint(a,b)
print(mylist[x])
random.shuffle(mylist)                      # Trộn ngẫu nhiên