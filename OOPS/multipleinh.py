class area:
    def area(self,l,b):
        return 2*l*b
    
class perimeter:
    def perimeter(self,l,b):
        return (1/2)*(l*b)

class rectangle(area,perimeter):
    pass

r=rectangle()
print("area of the rectangle is",r.area(5,6))
print("perimeter of the rectangle is",r.perimeter(5,6))
