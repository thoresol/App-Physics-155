#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 10:55:26 2021

@author: scfortuna
"""

import numpy as np

def f1(x):
    return np.sin(x)**2 + np.cos(2*x)**3

def f2(x):
    return 1E20*x**2

def f3(x):
    return 1E-20*x**2

def f4(x):
    return np.sin(x/np.pi)