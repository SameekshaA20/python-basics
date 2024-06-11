a= ["Mysore","Blore","Mlore"]
a.insert(1,"Mandya")
a.append("Coorg")
print(a)

x = ["Dosa","Idli"]
y = ["tea","coffee"]
x.extend(y)
x.remove("tea")
print(x)
for X in x:
    print(X)
a.pop(2)
print(a)

A=["apple","orange","banana"]
A.sort()
print(A)
B=[55,2,98,23]
B.sort(reverse=True)
print(B)
B=A.copy()
print(B)
C=[76,98,55]
