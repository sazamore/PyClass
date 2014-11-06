#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
simple_script.py

Generate and plot a histogram of random data.

Created on Tue Nov 04 17:38:57 2014
@author: Sharri
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(0,2,(75,1));
plt.figure()
plt.hist(x)