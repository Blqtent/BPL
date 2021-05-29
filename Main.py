#scroll to line 61 to program
# BPL Library Don't mess with it #
#some vars
import time
mem = [
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
]
#the output library
class output:
  def writeStr(x):
    print(str(x))
    if type(x) != str:
      raise ValueError
  def writeInt(x):
    print(int(x))
#the keyboard library, very short lol
class keyboard: 
  def keyIn(x):
    input(x)
#the memory library 
class memory:
  def memSet(addr,data):
    mem[addr] = data
  def memGet(addr):
    print(mem[addr])
#the math library pretty long
class math:
  def mul(a,b):
    print(a*b)
  def div(a,b):
    print(a/b)
  def min(a,b):
    if a < b:
      return a 
    else:
      return b
  def max(a,b):
    if a > b:
      return a
    else:
      return b
  def sqr(a):
    return a**2
  def exp(a,b):
    print(a**b)
  def sqrt(a):
    return int(a ** 0.5)
#system library very short too
class sys:
  def pause(x):
    time.sleep(x)
  def error(errnum):
    print("ERROR: code: <",errnum,">")
# @ DiamondCoder1000


#your code here

#hello world program:

class Main:
  memory.memSet(0,"Hello, world!")
  memory.memGet(0)
