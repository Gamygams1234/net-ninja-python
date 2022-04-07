belts = {"Gamy": "blue", "Chris": "red"}

print(belts["Gamy"])

# this will error
# print(belts[0])

# this will return false
print("Cullen" in belts)

# this will return true
print("Chris" in belts)

print(list(belts.keys()))
print(list(belts.values()))

# adding a belt
belts["Cullen"] = "black"

print(list(belts.keys()))
print(list(belts.values()))