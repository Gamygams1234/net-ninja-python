class Planet:
  def __init__(self):
    self.name = "Hoth"
    self.radius = 200000
    self.gravity = 5.5
    self.system = "Hoth Systems"

  def orbit(self):
    print(self.name+ " is orbiting")


hoth = Planet()

print(hoth.name)
print(hoth.radius)
print(hoth.gravity)
hoth.orbit()