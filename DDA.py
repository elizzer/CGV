

start=input("Enter the first coordinate: ").split(",")
end=input("Enter the last coordinate: ").split(",")

x1,y1=int(start[0]),int(start[1])
x2,y2=int(end[0]),int(end[1])


print(start)
print(end)
print(x1,y1)
print(x2,y2)

m=(y2-y1)/(x2-x1)

print("The slope is ",m)
yk=y1
xk=x1
if(m<=1):
    while(yk<=y2 and xk<=x2):
        yk1=yk+m
        print(int(yk1),xk)
        xk+=1
        yk=yk1
else:
    while(yk<=y2 and xk<=x2):
        xk1=xk+(1/m)
        print(int(yk),int(xk1))
        yk+=1
        xk=xk1

