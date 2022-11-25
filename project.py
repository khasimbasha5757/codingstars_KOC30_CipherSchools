n=int(input("Enter a number: "))
print("Tables upto n is")
for i in range(1,11):
    for j in range(2,n+1):
        print(j, 'x', i, '=', i*j, "\t","\t","\t","\t", end="")
    print()