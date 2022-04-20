# Get triangle ariea with 3 sides
import math
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
S = (a+b+c)/2

if (a+b) > c and (a+c) > b and (b+c) > a:
    area = math.sqrt(S*(S-a)*(S-b)*(S-c))
    print(area)

else:
    print("Triangle is not Possible.")
