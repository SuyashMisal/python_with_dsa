#area of circle
a=int(input("enter the dia of circle"))
b=(3.14/4)*(a*a)
print("area of circle=",b)
#area of rectrangle
A=int(input("enter b"))
B=int(input("enter d"))
C=A*B



a=int(input("Enter breadth of rectangle:"))
b=int(input("Enter depth of rectangle:"))
c=(a+b)*2
print("perimeter of rectangle:",c)


number=-4
if number>0:
    print("positive num")
elif number<0:
    print("negative num")
else:
    print("numberis zero")



a=10
b=20
a,b=b,a
print(a)
print(b)
#convert km into meters
a=int(input("enter Km:"))
b=1000
c=a*b
print("meters",c,"m")
#converts minits to hours 
A=int(input("enter minits:"))
B=60
C=A/B
print("in hour=",C,"h")


#calculet simple intrest
a=int(input("Engter yor amount"))
b=int(input("Enter rate of intrest"))
c=int(input("time"))
d=(a*b*c)/100
print("simple intrest=",d)