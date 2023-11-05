import matplotlib.pyplot as plt
import numpy as np

failo_vardas = 'data_0001.txt'
failas = open(failo_vardas, mode='r', encoding='utf-8')
turinys = failas.read()
print(turinys.split())
x = []
y = []
for i in turinys:
    a = i.split(';')
    # print(a)
    x.append(float[a[5]])
    y.append(float[a[5]])
print(x)
print(y)

failo_vardas.close()