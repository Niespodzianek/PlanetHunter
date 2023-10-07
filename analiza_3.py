#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 20:25:15 2023

@author: michal
"""
import lightkurve as lk
import matplotlib.pyplot as plt

# cel badania
TIC = "TIC 55525572"

# dane celu badania
data = lk.search_lightcurve(TIC)
# print(data)
data_1 = lk.search_lightcurve(TIC, author = "SPOC")
# print(data_1)
data_2 = lk.search_lightcurve(TIC, author="SPOC", sector=4)
# print(data_2)

# filtr daje wynik równy zmiennej data_1
filtr = (data.author == "SPOC")
# print(data[filtr])

# normalizacja dla pomiaru jednego sektora
lc_data_2 = data_2.download()
# przed normalizacją
lc_data_2.plot(linewidth = 0, marker = ".", color = "blue", alpha = 0.5)
# po normalizacji
lc_data_2.normalize().plot(linewidth = 0, marker = ".", color = "red", alpha = 0.5)

# normalizacja dla pomiaru wielu sektorów
mask = (data.author == "SPOC")
multi_data = data[mask][1:4]
print(multi_data)

lc_multi_data = multi_data.download_all()
# przed normalizacją
lc_multi_data.plot()
# normalizacja metodą stitch()
lc_multi_normalized = lc_multi_data.stitch()
# po normalizacji
lc_multi_normalized.plot(linewidth = 0, marker = ".", color = "black", alpha = 0.5)

# uśrednianie wyników przez dzielenie danych na 15 minutowe sekwencje czasowe
bin_time = 15/24/60
lc_multi_normalized_binned = lc_multi_normalized.bin(bin_time)
lc_multi_normalized_binned.plot()

fig, ax = plt.subplots(figsize = (10, 5))
lc_multi_normalized.plot(ax = ax, linewidth = 0, marker = ".", color = "blue", markersize = 1)
lc_multi_normalized_binned.plot(ax = ax, linewidth = 0, marker = ".", color = "red", markersize = 1)
