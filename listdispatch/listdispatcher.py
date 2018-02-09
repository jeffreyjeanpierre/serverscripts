names_list = []

def ask():
'''This function will take input for
   the amount of names to add to the
   names_list list.'''
  global names_list
  counter = 1
  while counter:
    try:
      count = int(raw_input("How many names: "))
      break
    except:
      print "Must be a number."
  while count > 0:
    placeholder = raw_input("Enter number %s's name: " % count)
    names_list.append(placeholder)
    count -= 1

def names():
'''This function will format the names list.
   Please run the run()
   function instead of using this.'''
  if len(names_list) > 1:
    for name in names_list:
      if name != names_list[-1]: print name +",",
    print "and " + name +"."
  else:
    for name in names_list: print name +"."

def run():
'''Run this after running ask().'''
  print("hello"),
  names()