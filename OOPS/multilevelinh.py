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

class average(marks):
    avg=0
    def average (self):
        self.avg=(self.s1+self.s2+self.s3)/3
        print("average marks of student is : ",self.avg)

a=average()
a.details() 
a.result() 
a.average