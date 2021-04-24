"""Graphing frequencies of die rolls with Seaborn."""
import matplotlib

import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import sys

rolls = [random.randrange(1, 7) for i in range(1, int(sys.argv[1]))]

print(rolls)