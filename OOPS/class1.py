class demo:
    "Example of a class"   #document string
    #instance variables
    id=10
    name="John"
    def function():
        print("Function called fromm a class")

print(demo.__doc__)
print(demo.id,demo.name)
demo.function()  #function call 
