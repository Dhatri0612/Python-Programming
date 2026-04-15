# s={1,2,3}
# s.add(4)
# print(s)

# s={10,20,30,40}
# s.remove(20)
# print(s)

# l = [1, 2, 2, 3, 4, 4]
# s=set(l)
# print(s)

# s={1,2,3,4}
# if 5 in s:
#     print("present")
# else:
#     print("not present")

# a = {1, 2, 3}
# b = {3, 4, 5}
# c=a.union(b)
# print(c)
# d=a.intersection(b)
# print(d)
# e=a.difference(b)
# print(e)

# s={1,2,3}
# s.update({4,5,6})
# print(s)

# s={1,2,3,4}
# print(s.pop())

# l1 = [1, 2, 3, 4]
# l2 = [3, 4, 5, 6]
# s1=set(l1)
# s2=set(l2)
# s=s1.intersection(s2)
# print(s)

# s = "programming"
# se=set()
# for i in range(len(s)):
#     se.add(s[i])
# print(se)

# a = {1, 2}
# b = {1, 2, 3, 4}
# print(a.issubset(b))

# l=[1,2,3,2,1,4]
# print(set(l))
# seen=set()
# duplicate=set()
# for num in l:
#     if num in seen:
#         duplicate.add(num)
#     else:
#         seen.add(num)
# print("Unique:", set(l))
# print("Duplicates:", duplicates)

# l = [1, 2, 3, 4, 5, 6]
# evenset=set()
# for num in l:
#     if num%2==0:
#         evenset.add(num)
# print(evenset)

# s = {1, 2, 3, 4, 5}
# for num in s.copy():
#     if num%2!=0:
#         s.remove(num)
# print(s)

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.isdisjoint(b))

# l = [10, 20, 30, 40]
# s=set()
# for num in l:
#     s.add(num*num)
# print(s)

# s = "hello world"
# s1=set(s)
# print(len(s1))

# l1 = [1, 2, 3, 4]
# l2 = [3, 4, 5, 6]
# s1=set(l1)
# s2=set(l2)
# print(s1.symmetric_difference(s2))

# l = [1, 2, 3, 4, 5]
# if len(l)==len(set(l)):
#     print("All elements are unique")
# else:
#     print("Duplicate present")

# l = [1, 2, 2, 3, 3, 4, 5]
# result=set()
# for num in l:
#     if l.count(num)==1:
#         result.add(num)
# print(result)

# s={1,2,3,4}
# copy_set=s.copy()
# s.add(5)
# print("Original:", s)
# print("Copy:", copy_set)

# s = "aabbccdde"
# for ch in s:
#     if s.count(ch)==1:
#         print(ch)
#         break

# l = [1, 2, 2, 3, 3, 4, 5, 5, 6]
# s=set()
# for num in l:
#     if l.count(num)>1:
#         s.add(num)
# print(s)
#  or 
l = [1, 2, 2, 3, 3, 4, 5, 5, 6]

seen = set()
duplicates = set()

for num in l:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)
