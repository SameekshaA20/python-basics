num = int(input("Enter a number"))
for i in range(2, num+1):
    for j in range(2, i-1):
        if i % j == 0:
            print(j)
