#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 00:37:59 2023

@author: michal
"""

import lightkurve as lk
import matplotlib.pyplot as plt
from astropy import units as u
import numpy as np

TIC = "TIC 55525572"
data = lk.search_lightcurve(TIC)

mask = data.author == "SPOC"
phase_folding_data = data[mask][-16:]

# pozyskanie danych i ich normalizacja
lc = phase_folding_data.download_all().stitch()

# phase folding
period = 83.8979
t0 = 2125.847
lc_phased = lc.fold(period = period, epoch_time = t0)

# uśrednianie w oknach 15 minutowych
lc_phased_binned = lc_phased.bin(15/24/60)

# wykres porównujący phase folding i phase folding po uśrednieniu
fig, ax = plt.subplots(figsize = (8, 5))
plt.xlim(-2, 2)
plt.ylim(0.9965, 1.0035)
lc_phased.plot(ax = ax, linewidth=0, marker=".", markersize=0.5, color="blue", alpha=0.5, label="phased")
lc_phased_binned.plot(ax = ax, linewidth=0, marker="o", markersize=1, color="black", alpha=0.9, label="phased and binned")

# linie wyznaczające zakres transit depth, z powyższego wykresu
plt.axhline(1)
plt.axhline(0.9993)
transit_depth = 1 - 0.9993
# promień gwiazdy w przeliczeniu na jednostki słoneczne
R_star = 2.04354 * u.Rsun
# promień planety w jednostce słońca
r_pl_solar_radius = np.sqrt(transit_depth) * R_star
# promień planety przeliczony na jednostkę ziemską
r_pl_earth_radius = r_pl_solar_radius.to(u.Rearth)
print(r_pl_solar_radius, r_pl_earth_radius)
