import geometry

print("1.Area of circle")
print("2.Area of rectangle")

choice=int(input("Enter your choice:"))

if(choice==1):
    radius=float(input("Enter the radius of circle:"))
    print(f"Area of circle:{geometry.area_circle(radius)}")
else:
    length=float(input("Enter the length of rectangle:"))
    breadth=float(input("Enter the breadth of reactangle:"))
    print(f"Area of circle:{geometry.area_rectangle(length,breadth)}")