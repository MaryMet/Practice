# pie chart using mathplot and numpy
# Author : MAry Metcalfe

import matplotlib.pyplot as plt
import numpy as np

possible_counties =["Mayo", "Tipp", "Dublin", "Wexford", "Sligo"]

counties = np.random.choice (possible_counties, p = [0.1, 0.3, 0.2, 0.12, 0.28], size = (100))

unique, counts = np.unique(counties, return_counts = True)

plt.pie (counts, labels = unique)
plt.show()
