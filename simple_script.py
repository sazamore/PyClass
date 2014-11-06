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

#make it into a function!
def show_normhist(data_length=1000, bins=100):
    """Create 1d data with normal distribution, then plot it as a histogram."""
    
    x = np.random.normal(0,2,data_length);
    plt.hist(x,bins)
    plt.show()

#wanna call it from the command line?
def main():
    show_normhist(10000,50) #call the function and give the paramaters, if applicable

#call function
if __name__ == '__main__':
    main()