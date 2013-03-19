#!/usr/bin/env python
# -*- Coding:utf-8 -*-
'''an eventplot showing sequences of events with various line properties
the plot is shown in both horizontal and vertical orientations'''

import matplotlib.pyplot as plt
import numpy as np

# set the random seed
np.random.seed(0)

# create random data
data1 = np.random.random([6, 50])

# set different colors for each set of positions
colors1 = np.array([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1],
                    [1, 1, 0],
                    [1, 0, 1],
                    [0, 1, 1]])

# set different line properties for each set of positions
# note that some overlap
lineoffsets1 = np.array([-15, -3, 1, 1.5, 6, 10])
linelengths1 = [5, 2, 1, 1, 3, 1.5]

fig = plt.figure()

# create a horizontal plot
ax1 = fig.add_subplot(221)
ax1.eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
              linelengths=linelengths1)
ax1.set_title('horizontal eventplot 1')


# create a vertical plot
ax2 = fig.add_subplot(223)
ax2.eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
              linelengths=linelengths1, orientation='vertical')
ax2.set_title('vertical eventplot 1')

# create another set of random data.
# the gamma distribution is only used fo aesthetic purposes
data2 = np.random.gamma(4, size=[60, 50])

# use individual values for the parameters this time
# these values will be used for all data sets (except lineoffsets2, which
# sets the increment between each data set in this usage)
colors2 = [[0, 0, 0]]
lineoffsets2 = 1
linelengths2 = 1

# create a horizontal plot
ax1 = fig.add_subplot(222)
ax1.eventplot(data2, colors=colors2, lineoffsets=lineoffsets2,
              linelengths=linelengths2)
ax1.set_title('horizontal eventplot 2')


# create a vertical plot
ax2 = fig.add_subplot(224)
ax2.eventplot(data2, colors=colors2, lineoffsets=lineoffsets2,
              linelengths=linelengths2, orientation='vertical')
ax2.set_title('vertical eventplot 2')

plt.show()