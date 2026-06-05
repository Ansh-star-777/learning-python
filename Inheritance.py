class Dad:
  def __init__(self,eye_colour,aggression):
    self.eye_colour = eye_colour
    self.aggression = aggression
  
  def display(self):
    print("Your eye colour is",self.eye_colour)
    print("aggresive:",self.aggression)

class Son(Dad):
  def __init__(self,eye_colour,aggression,name,age):
    self.name = name
    self.age = age

    super().__init__(eye_colour,aggression)

ansh = Son("Dark brown",False,"Ansh",13)
ansh.display()
# dad_1 = Dad("Dark brown",False)
# dad_1.display()
