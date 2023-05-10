x=int(input("Enter the range to print cubic of numbers: "))
print(f"Cubic of numbers between 0 and {x-1}")
for i in range(x):
    print(i,": ",i**3)
