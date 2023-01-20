print("Largest number")

a = int(input("Enter First num\n"))
b = int(input("Enter Second Num\n"))
c = int(input("Enter Third num\n"))


if(a > b) and (a > c):
        largest = a

elif(b > a) and (b > c):
    largest = b

else:
    largest = c


print("Largest number is",largest)    
