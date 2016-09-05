## This algo find a list of number
## pick from set
## that sum to TARGET
## and whom len is maxSize
## It is nto very efficient
TARGET  = 64

BACK = -1
STOP = 0
FORWARD = 1

bags=[9,8,7,6,5,4,3,2,1]

maxSize = 23

path=[]

def addMoar(v):
  path.append(v)
  print path
  with open("path.txt","a") as f:
    f.write(str(path))
    f.write("\n")
  #raw_input("Press Enter to continue...")
  if (len(path) > maxSize) or (sum(path) > TARGET):
    path.pop()
    return BACK
  if (len(path) == maxSize) and (sum(path) == TARGET):
    return STOP
  for v in bags:
    rep = addMoar(v)
    if rep == FORWARD: 
      continue
    if rep == STOP:
      return STOP
  path.pop()
  return BACK


addMoar(7)

print"*"*20
print(len(path))
print(sum(path))
print path
