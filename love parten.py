
print("only works when input is less than 9")
x = int(input("enter height of symbol"))


y=x-1
k=0
while k<=y:
    if k==0 or k==y or k==y//2:
         print(" ",end="")
    else:
        print("x",end="")
    k=k+1
print("")
k=0
while k<=y:
    if k==0 or k==y or k==y//2:
         print("x",end="")
    else:
        print(" ",end="")
    k=k+1
print("")

i=0
while i<=y:
    j=0
    while j<=y:
        if j==i or j==y-i:
            print("x",end="")
        else:
            print(" ",end="")
        j=j+1
    print(" ")
    i=i+1
    if i==y//2+1:
        break
print("")


