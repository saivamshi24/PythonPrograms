class student:
    id=10
    name="john"
    def details(self):
        print("student details are id %d name %s"%(self.id,self.name))

class marks(student):
    s1=85
    s2=95
    s3=75
    def result(self):
        print("s1 %d s2 %d s3 %d"%(self.s1,self.s2,self.s3))

m=marks() #object creation
m.details()
m.result()               