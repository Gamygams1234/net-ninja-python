# variable scope
# global scop
my_name = "Gamy"

def print_name():
  # can be overriden
  #we can update it to go global my_name then my_name = Jonn
  my_name = "John"
  print("The name inside the fuction is", my_name)

  

print("the name outside the function is", my_name)

print_name()