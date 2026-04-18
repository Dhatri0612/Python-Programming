def comapre(a,b):
    if(a>b):
        print(a,"is greater")
    else:
        print(b,"is greater")

a=10
b=20
comapre(a,b)




#  Lambda function (small function bnane k liye usee krte h like in simgle line)

# def double(x):
#     return x*2
# print(double(5))

double =lambda x:x*2
print(double(5))

cube= lambda x:x*x*x
print(cube(5))

average=lambda x,y:(x+y)/2
print(average(4,6))

#  function m bhii function pass kr skte h
def appl(fx,value):
    return 6+fx(value)
print(appl(cube,2))
print(appl(lambda x:x*x*x,2))