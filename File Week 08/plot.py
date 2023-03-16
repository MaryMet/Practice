# messing with plots/mathlab
# plots lines
# Author : Mary Metcalfe

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array (range (1, 100))
ypoints = xpoints * xpoints

plt.plot (xpoints, ypoints)
plt.show()