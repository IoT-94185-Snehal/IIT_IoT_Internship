import math

radius = 5
area = math.pi * math.pow(radius,2)
print(f"The area of circle = {area}")

angle_degrees = 30
angle_radians = math.radians(angle_degrees)
print(f"{angle_degrees} degree is = {angle_radians}radians")

math.sqrt(25)
print(f"sqrt={math.sqrt(25)}")




import os

print("Current working directory:", os.getcwd())
print("List of files/folders here:", os.listdir())

test_dir = "my_test_dir"
if not os.path.exists(test_dir):
    os.mkdir(test_dir)
    print(f"Created folder {test_dir}")

# Clean up
if os.path.exists(test_dir):
    os.rmdir(test_dir)
    print(f"Removed folder {test_dir}")