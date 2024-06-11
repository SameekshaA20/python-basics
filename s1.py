for i in range(5):
    for j in range(5):
        print("*", end="\t")
    print(end="\n")

num = 5
for i in range(num, 0, -1):
    for j in range(num-i):
        print(" ", end=" ")
    for k in range(i, 0, -1):
        print(k, end=" ")
    print()

