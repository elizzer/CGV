
start=input("Enter the first coordinate: ").split(",")
end=input("Enter the last coordinate: ").split(",")

x1,y1=int(start[0]),int(start[1])
x2,y2=int(end[0]),int(end[1])

dx=x2-x1
dy=y2-y1

p0=2*dy-dx

xk=x1
yk=y1

m=dy/dx
l=[(xk,yk)]
if m<=1:
    pk=p0
    for i in range(dx-1):
        xk+=1
        if pk<0:
            print(xk,yk)
            l.append((xk,yk))
            pk=pk+2*dy
        else:
            yk+=1
            print(xk,yk)
            l.append((xk,yk))
            pk=pk+2*dy-2*dx

l.append((x2,y2))
print(l)

