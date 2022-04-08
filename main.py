class Planet:
  def __init__(self, name, radius, gravity,system):
    self.name = name
    self.radius = radius
    self.gravity = gravity
    self.system = system

  def orbit(self):
    print(self.name+ " is orbiting")


hoth = Planet("Hoth",200000,5.5, "Hoth Systems")

print(hoth.name)
print(hoth.radius)
print(hoth.gravity)
hoth.orbit()
