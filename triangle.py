def distance(xi,yi,xj,yj):
    return (((xi-xj)**2+(yi-yj)**2)**0.5)

def istrangle(max,a,b):
    if(a+b>max):
        print("Trangle")
    else:
        print("not a trangle")
data=" exit"
while data!='exit':
    x1=float(input("Enter the value of first point:"))
    y1=float(input("Enter the value of first point:"))
    x2=float(input("Enter the value of second point:"))
    y2=float(input("Enter the value of second point:"))
    x3=float(input("Enter the value of third point:"))
    y3=float(input("Enter the value of third point:"))

    d1=distance(x1,y1,x2,y2)
    print(f'\n the distance d/w ({x1},{y1}) and ({x2},{y2})is={d1} ')


    d2=distance(x2,y2,x3,y3)
    print(f'\n the distance d/w ({x2},{y2}) and ({x3},{y3})is={d2} ')


    d3=distance(x3,y3,x1,y1)
    print(f'\n the distance d/w ({x3},{y3}) and ({x1},{y1})is={d3} ')

    if (d1>d2):
        if(d1>d3):
            istrangle(d1,d2,d3)
        else:
            istrangle(d3,d1,d2)
    elif (d2>d3):
        istrangle(d2,d3,d1)
    else:
        istrangle(d3,d2,d1)