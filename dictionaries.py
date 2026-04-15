# dict={"name": "Dhatri", "age": 21}
# print(dict["name"])
# print(dict.get("age"))

# d = {"a": 1, "b": 2}
# d["c"]=3
# print(d)

# d = {"x": 10, "y": 20, "z": 30}
# d.pop("y")
# print(d)

# d = {"a": 1, "b": 2}
# if "a" in d:
#     print("present")
# else:
#     print("Not present")

# d = {"a": 10, "b": 20, "c": 30}
# total=0
# for val in d.values():
#     total+=val
# print(total)
# print(sum(d.values()))

# s = "apple"
# d={}
# for ch in s:
#     if ch not in d.keys():
#         d.update({ch:s.count(ch)})
# print(d)
# or
# s="apple"
# d={}
# for ch in s:
#     if ch in d:
#         d[ch]+=1
#     else:
#         d[ch]=1
# print(d)

# l = [1, 2, 2, 3, 3, 3]
# d={}
# for num in l:
#     if num in d:
#         d[num]+=1
#     else:
#         d[num]=1
# print(d)

# d = {"a": 1, "b": 2, "c": 3}
# newd={}
# for key,val in d.items():
#     newd[val]=key
# print(newd)

# d = {"a": 10, "b": 5, "c": 15}
# max_key=None
# max_val=0
# for key,val in d.items():
#     if max_val<val:
#         max_key=key
#         max_val=val
# print("Max key: ", max_key)
# print("Max val: ",max_val)

# s = "aabbccdde"
# d={}
# for ch in s:
#     if ch in d:
#         d[ch]+=1
#     else:
#         d[ch]=1
# print(d)
# for key,val in d.items():
    