# -*- coding: utf-8 -*-
"""
# scipy.cluster - кластеризація
Кластеризація (кластерний аналіз) - задача розбиття множини об'єктів на групи (кластери) подібних об'єктів. В прикладі показана кластеризація методом k-середніх, який оснований на мінімізації сумарного квадратичного відхилення точок кластерів від центрів цих кластерів. Спробуйте також потужній алгоритм кластеризації даних з наявністю шуму `sklearn.cluster.DBSCAN`.
"""
import numpy
from scipy.cluster import vq
import matplotlib.pyplot as plt

# масиви випадкових точок з координатами x,y
c1 = numpy.random.randn(100, 2) + 5 
c2 = numpy.random.randn(30, 2) - 5
c3 = numpy.random.randn(50, 2)
data = numpy.vstack([c1, c2, c3]) # об'єднати дані

whiten=vq.whiten(data) # нормалізувати дані
centroids,labels=vq.kmeans2(whiten,3) # центроїди і мітки 3-x кластерів
#plt.scatter(data[:,0],data[:,1],c=labels); plt.show()

# або
centroids, distortion = vq.kmeans(data, 3) # centroids - центроїди 3-х кластерів методом k-середніх, distortion - сума квадратів відстаней між точками і відповідною центроїдою
identified, distance = vq.vq(data, centroids) # масив для ідентифікації та масив з відстанями до центроїди
# координати точок та відстані до центроїди в кожному кластері
vqc1,d1 = data[identified == 0], distance[identified == 0] 
vqc2,d2 = data[identified == 1], distance[identified == 1]
vqc3,d3 = data[identified == 2], distance[identified == 2]
plt.figure()
plt.scatter(vqc1[:,0],vqc1[:,1],c='r',s=d1*20) # точки кластера 1
plt.scatter(vqc2[:,0],vqc2[:,1],c='g',s=d2*20) # точки кластера 2
plt.scatter(vqc3[:,0],vqc3[:,1],c='b',s=d3*20) # точки кластера 3
plt.scatter(centroids[:,0], centroids[:,1], marker='o', s=10000, c='k', alpha=0.2) # центроїди
plt.xlabel("x");plt.ylabel("y");plt.grid();plt.show()
"""
Рисунок - Результати кластеризації
"""
