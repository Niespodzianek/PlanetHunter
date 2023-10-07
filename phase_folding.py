#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 00:37:59 2023

@author: michal
"""

import lightkurve as lk
import matplotlib.pyplot as plt

TIC = "TIC 55525572"
data = lk.search_lightcurve(TIC)

mask = data.author == "SPOC"
phase_folding_data = data[mask][0:9]

print(phase_folding_data)

# pozyskanie danych i ich normalizacja
lc = phase_folding_data.download_all().stitch()

fig, ax = plt.subplots(figsize = (8, 4))
lc.plot(ax = ax, linewidth=0, marker=".", markersize=1, color="blue", alpha=0.5, label="po normalizacji")
plt.xlim(1558, 1583)

# phase folding
period = 83.8979
t0 = 2125.847
lc_phased = lc.fold(period = period, epoch_time = t0)
lc_phased.plot(linewidth=0, marker=".", markersize=1, color="red", alpha=0.5, label="phase folding")

# uśrednianie w oknach 15 minutowych
lc_phased_binned = lc_phased.bin(15/24/60)

# wykres porównujący phase folding i phase folding po uśrednieniu
fig, ax = plt.subplots(figsize = (8, 5))
lc_phased.plot(ax = ax, linewidth=0, marker=".", markersize=0.5, color="blue", alpha=0.5, label="phased")
lc_phased_binned.plot(ax = ax, linewidth=0, marker="o", markersize=1, color="black", alpha=0.9, label="phased and binned")

plt.axhline(1)
plt.axhline(0.9989)
plt.xlim(-2, 2)
plt.ylim(0.9965, 1.0035)

print(lc_phased_binned)
