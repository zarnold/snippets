## This algo find a list of number
## pick from set
## that sum to TARGET
## and whom len is maxSize
## It is nto very efficient
TARGET  = 38

BACK = -1
STOP = 0
FORWARD = 1

bags=[7,5,3,1]

maxSize = 10

path=[]

def addMoar(v):
  path.append(v)
  print path
  with open("path.txt","a") as f:
    f.write(str(path))
    f.write("\n")
  print("Sum: %d"%sum(path))
  #raw_input("Press Enter to continue...")
  print(len(path))
  if (len(path) > 10) or (sum(path) > TARGET):
    print("opo")
    path.pop()
    return BACK
  if (len(path) == 10) and (sum(path) == TARGET):
    return STOP
  for v in bags:
    print(v)
    rep = addMoar(v)
    if rep == FORWARD: 
      continue
    if rep == STOP:
      return STOP
  path.pop()
  return BACK


addMoar(7)

