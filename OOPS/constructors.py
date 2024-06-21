class example:
  #def __init__(self):
      #print("default constructor called")

   def __int__(self,x,y):
      print("parameterized constructor called",x,y)

         
   def __del__(self):
      print("destructor called")

e=example(10,20)
