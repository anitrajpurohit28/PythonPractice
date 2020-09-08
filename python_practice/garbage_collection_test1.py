import time
import gc
class Test:
    def __init__(self):
        print("constructor called")
    def __del__(self):
        print("Destructor called")

gc.disable()
print(gc.isenabled())

t1 = Test()
t1 = None
# del t1 # this will also lead to garbage collection
time.sleep(10)
print("End of application")
