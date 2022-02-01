#find area,perimeter of polygon 
import math
PI=math.pi
def c_area(r):
    return PI*r*r
def c_perimeter(r):
    2*PI*r
def rect_area(l,b):
    return l*b
def rect_perimeter(l,b):
    return 2*(l+b)


polygon=' '
while ( polygon !='exit'):
    print("\npolygon\ncircle\nrectrangle\nexit")
    polygon=input("Enter the properties of polygon or exit: ")
    properties=' '
    if (polygon=="circle"):
        r=float(input("Enter the value of radious:"))
        while (properties==' '):
            print("\ncircleproperties\narea\nperimeter\nback")
            properties=input("Enter the properties of circle or go back:")
            if (properties=="area"):
                circle_area=c_area(r)
                print(f'\n the area of circle with given {r} ={circle_area} meter')
                properties=''
            elif(properties=="perimeter"):
                circle_perimeter=c_perimeter(r)
                print(f'\n the perimeter of circle with given {r}={circle_perimeter}sq. meter')
                properties=''
            elif(properties=="back"):
                print("back")
                break
            else:
                print("please enter the value proprties again")
            properties=' '
    elif(polygon=="rectrangle"):
        l=float(input("Enter the velue of lenth:"))
        b=float(input("Enter the value of breath:"))
        while(properties==" "):
            print("\nrectrangle\narea\nperimeter\nback")
            properties=input("Enter the properties of rectrangle:")
            if (properties=="area"):
                rectangle_area=rect_area(l,b)
                print(f'\n the area of rectangle with {l} and {b}={rectangle_area} sq.meter')
                properties=' '
            elif(properties=='perimeter'):
                rectangle_perimeter=rect_perimeter(l,b)
                print(f'\n the perimeter of rectrangle  with {l} and {b}={rectangle_perimeter} meter')
                properties=' '
            elif(properties=="back"):
                print("back")
                break
            else:
                print("Kindly Enter the properties again")
            properties=' '
    elif(polygon=="exit"):
        break
    else:
        print("kindly enter the polygon again")
    


