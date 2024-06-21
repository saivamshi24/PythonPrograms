from Exception2 import NameLengthError

def validate(username):
    if(len(username)<8):
        raise NameLengthError("minimum eight characters required")
    else:
        print("its a valid username")

try:
    validate(input("username required"))
    print("thank you")

except Exception as e:
    print("validation failure because: ",e)

finally:
    print("program ended")                