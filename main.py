class Planet:
  shape = "round"
  def __init__(self, name, radius, gravity,system):
    self.name = name
    self.radius = radius
    self.gravity = gravity
    self.system = system

  def orbit(self):
    print(self.name+ " is orbiting")

  # this is a class method that only takes in the class variables
  @classmethod
  def commons(cls):
    return f'All planets are {cls.shape} because of gravity'
  @staticmethod
  def spin(speed= "2000 mph"):
    return f'The planet spins at {speed}'
    


hoth = Planet("Hoth",200000,5.5, "Hoth Systems")
earth = Planet("Earth",200000,5.5, "The government")

print(hoth.name)
print(hoth.radius)
print(hoth.gravity)
print(hoth.shape)


print("The earth shape is " +hoth.shape)
hoth.orbit()
# this is the commons method amongst all of them
print(earth.commons())

# this is the static methods that can be overridden
print (earth.spin("400mph"))

print (hoth.spin())
