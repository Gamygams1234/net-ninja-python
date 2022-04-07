belts = {}

while True: 
  name = input("Enter a name")
  belt = input("Enter a belt")
  belts[name] = belt

  another = input("Another yes or no?")
  if (another =="yes"):
    continue
  else:
    break


print(belts)
