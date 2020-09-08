import gc
print("Default: isenabled[{}]".format(gc.isenabled()))
gc.disable()
print("gc.disable executed: isenabled[{}]".format(gc.isenabled()))
gc.enable()
print("gc.disable executed: isenabled[{}]".format(gc.isenabled()))
