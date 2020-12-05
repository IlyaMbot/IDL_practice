#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import astropy.io.fits as fitsr
import matplotlib.pyplot as plt

filename = "./hmi.m_45s.2011.10.27_04_06_45_TAI.magnetogram.fits"

image_file = fitsr.open(filename)
print(image_file.info())

image_data = fitsr.getdata(filename)
print(type(image_data))
print(image_data.shape)



plt.imshow(image_data, cmap='magma')
plt.colorbar()

