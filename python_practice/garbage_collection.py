import time
import sys
class Test:
    def __init__(self):
        print("Constructor called...")
    def __del__(self):
        print("Destructor called...")

t1 = Test()
t2 = t1
t3 = t2
t4 = t3
print("Object reference:\tt1: {}\tt2: {}\tt3: {}\tt4: {}".format(
      sys.getrefcount(t1),
      sys.getrefcount(t2),
      sys.getrefcount(t3),
      sys.getrefcount(t4)))
del t1
time.sleep(10)
print("del t1 executed, Object ref: ", sys.getrefcount(t2))
time.sleep(5)

del t2
time.sleep(10)
print("del t2 executed, Object ref: ", sys.getrefcount(t3))
time.sleep(5)

del t3
time.sleep(10)
print("del t3 executed, Object ref: ", sys.getrefcount(t4))
time.sleep(5)
print("t3 sleep finished")
del t4
print("del t4 executed")
time.sleep(10)
print("End of application")
