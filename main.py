# for n in range(5):
#   print(n)


# from 3 to 9
for n in range(3, 10):
  print(n)


# going  by 4 including the 0
# for n in range(0, 20,4):
#   print(n)

burgers = ['beef', "checken", 'birria']


for n in range(len(burgers)):
  print(burgers[n])

# this is going backward in the range
for n in range(len(burgers)-1, -1, -1):
  print(burgers[n])