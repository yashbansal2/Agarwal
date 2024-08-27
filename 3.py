# only this shape valid square, rectngle, circle and triangle
a=input("enter the shape")
if a=="square":
    b=int(input("suggest its lenght also"))
    area=b*b
    print(area)
elif a=="rectangle":
    b=int(input("suggest its lenght also"))
    c=int(input("suggest its lenght also"))
    area=b*c
    print(area)
elif a=="circle":
    b=int(input("suggest its lenght also"))
    area=3.14*b*b
    print(area)
elif a=="triangle":
    b=int(input("suggest its lenght also"))
    c=int(input("suggest its lenght also"))
    area=0.5*b*c
    print(area)

