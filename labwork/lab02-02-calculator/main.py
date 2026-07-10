# this is the starting file for Lab Activity 2.2
print()
print("Area and Perimeter")

print()
# Get input
length_r = float(input("Please Enter Length: \t"))
width_r = float(input("Please Enter Width: \t"))

# Calculate the area and perimeter
area = (length_r * width_r)
perimeter = (length_r * 2)+(width_r * 2)
area = round(area, 2)
perimeter = round(perimeter, 2)
#format result
print()
print(f"Area: ", area)
print(f"Perimeter: ", perimeter)
print()
print("Toodles")
