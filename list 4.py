myuniquelist = [] 
myleftovers = []

def key():
   c = input()
   if c in myuniquelist:
      myleftovers.append(c)
      return False
   else:
      myuniquelist.append(c)
      return True

key() 
key()
key()
key()
key() 
key()

print("myuniquelist", myuniquelist)
print("myleftovers", myleftovers)