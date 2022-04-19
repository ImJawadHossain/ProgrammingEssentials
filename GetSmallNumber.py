# Get small number
a = float(input("Enter the 1st number:"))
b = float(input("Enter the 2nd number:"))
c = float(input("Enter the 3rd number:"))

if a < b and a < c:
    print(a, "is the smallest number.")

elif b < a and b < c:
    print(b, "is the smallest number.")

else:
    print(c, "is the smallest number.")
