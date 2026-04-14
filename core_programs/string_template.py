template= "Hello <<UserName>>, How are you?"
name=input("Enter your name: ")
if len(name)<3:
    print("name should have atleast 3 char ")
else:
    result=template.replace("<<UserName>>",name)
    print(result)