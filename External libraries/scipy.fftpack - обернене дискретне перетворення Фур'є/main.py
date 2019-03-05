# -*- coding: utf-8 -*-
"""
# scipy.fftpack - обернене дискретне перетворення Фур'є
Обернене дискретне перетворення Фур'є повертає сигнал за спектром його частот. В прикладі показано застосування прямого і оберненого дискретного перетворення Фур'є для частотного фільтрування сигналу.
"""
import numpy as np
from scipy.fftpack import rfft, irfft, fftfreq
import matplotlib.pyplot as plt
time   = np.linspace(0,2,2000) # час
signal = np.cos(5*np.pi*time) + 2*np.cos(7*np.pi*time) # сигнал
W = fftfreq(signal.size, d=time[1]-time[0]) # частоти
f_signal = rfft(signal) # спектр (дискретне перетворення Фур'є для дійсних)
cut_f_signal = f_signal.copy() # копія сигналу
cut_f_signal[(W<6)] = 0 # фільтруємо сигнал (відкидаємо частоти<6)
cut_signal = irfft(cut_f_signal) # відфільтрований сигнал (обернене дискретне перетворення Фур'є для дійсних)

plt.subplot(121); plt.plot(time,signal); plt.xlabel('t'); plt.ylabel('y')
plt.subplot(122); plt.plot(time,cut_signal); plt.xlabel('t')
plt.show(); print "Рисунок - Початковий і відфільтрований сигнал"

plt.figure()
plt.subplot(121); plt.plot(W,f_signal); plt.xlim(0,10); plt.xlabel('f'); plt.ylabel('A')
plt.subplot(122); plt.plot(W,cut_f_signal); plt.xlim(0,10); plt.xlabel('f')
plt.show(); print "Рисунок - Спектр початкового і відфільтрованого сигналу"
