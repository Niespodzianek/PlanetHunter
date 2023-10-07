#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 20:25:15 2023

@author: michal
"""
import lightkurve as lk

# cel badania
TIC = "TIC 470710327"

# dane celu badania
data = lk.search_lightcurve(TIC)
print(data)
data_1 = lk.search_lightcurve(TIC, author = "SPOC")
print(data_1)
data_2 = lk.search_lightcurve(TIC, sector=17)
print(data_2)

for data in data_2:
    lc = data.download()
    lc.plot(linewidth = 0, marker = ".", color = "blue", alpha = 0.5)
    lc.normalize().plot(linewidth = 0, marker = ".", color = "red", alpha = 0.5)

lc = data_2.download_all()
lc.plot(linewidth = 0, marker = ".", color = "blue", alpha = 0.5)
lc_multi = lc.stitch()
lc_multi.plot(linewidth = 0, marker = ".", color = "red", alpha = 0.5)

# # filtr daje wynik równy zmiennej data_1
# filtr = (data.author == "SPOC")
# # print(data[filtr])

# # normalizacja dla pomiaru jednego sektora
# lc_data_2 = data_2.download()
# # przed normalizacją
# lc_data_2.plot(linewidth = 0, marker = ".", color = "blue", alpha = 0.5)
# # po normalizacji
# lc_data_2.normalize().plot(linewidth = 0, marker = ".", color = "red", alpha = 0.5)

# # normalizacja dla pomiaru wielu sektorów
# mask = (data.author == "SPOC")
# multi_data = data[mask][0:4]
# print(multi_data)

# lc_multi_data = multi_data.download_all()
# # przed normalizacją
# lc_multi_data.plot()
# # normalizacja metodą stitch()
# lc_multi_normalized = lc_multi_data.stitch()
# # po normalizacji
# lc_multi_normalized.plot(linewidth = 0, marker = ".", color = "red", alpha = 0.5)

