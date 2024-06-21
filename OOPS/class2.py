class demo:
    "Example of a class"   #document string
    #instance variables
    id=10
    name="John"
    def function(self):
        print("Function called fromm a class",self.id,self.name)

object=demo() #object creation
print(object.__doc__)
print(object.id,object.name)
object.function()