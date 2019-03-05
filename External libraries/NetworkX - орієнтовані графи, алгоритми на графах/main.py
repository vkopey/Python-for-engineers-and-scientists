# -*- coding: utf-8 -*-
"""
# NetworkX - орієнтовані графи, алгоритми на графах
Ребра графа, які мають напрямок, називають дугами. Неорієнтований граф містить тільки ребра, а орієнтований граф містить тільки дуги. В NetworkX орієнтовані графи створюються за допомогою класу `DiGraph`. В прикладі показані операції з орієнтованими графами і розповсюджені алгоритми на графах (http://networkx.github.io/documentation/stable/reference/algorithms/index.html).
"""
import networkx as nx
import matplotlib.pyplot as plt
G=nx.DiGraph() # створити орієнтований граф
G.add_weighted_edges_from([(1,2,0.5), (1,3,0.5), (3,4,0.25)]) # додати ребра з вагами

print 'suc', list(G.successors(1)) # вузли-нащадки
print 'pre', list(G.predecessors(1)) # вузли-предки
print 'nei', list(G.neighbors(1)) # вузли-сусіди
print 'out', G.out_edges(1) # вихідні ребра
print 'in', G.in_edges(1) # вхідні ребра

print G.degree(1) # кількість ребер цього вузла. Але:
print G.degree(1, weight='weight') # сума ваг ребер цього вузла
print G.out_degree(1, weight='weight') # сума ваг вихідних ребер цього вузла
G2=G.reverse() # обернений граф
G2=G.subgraph([1,3,4]) # підграф
# див. також функції union, disjoint_union, cartesian_product, compose, complement
print G.has_edge(1,2) # чи граф має ребро 1,2
print G.has_node(1) # чи граф має вузол 1
print G.has_predecessor(2,1) # чи вузол 2 має предка 1
print G.has_successor(1,2) # чи вузол 1 має нащадка 2
print list(G.nodes_with_selfloops()) # вузли з ребрами, які виходять і входять в цей вузол
print list(G.selfloop_edges()) # ребра з однаковим вузлом на двох кінцях

nx.draw_spectral(G, with_labels=True) # нарисувати граф
plt.show(); print "Рисунок - Візуалізація орієнтованого графа"

# Алгоритми на графах:
print nx.is_tree(G) # чи це дерево?
try: print nx.find_cycle(G) # чи є цикли?
except: print "No cycle found"
print list(nx.dfs_edges(G,1)) # ітерація по ребрам для пошуку в глибину
print list(nx.bfs_edges(G,1)) # для пошуку в ширину (починати з 1)
print dict(nx.all_pairs_shortest_path(G)) # найкоротший шлях між усіма вузлами
print nx.shortest_path(G,1,4) # найкоротший шлях від 1 до 4
print nx.dijkstra_path(G,1,4) # або
print 'PageRank', nx.pagerank(G, alpha=0.9) # алгоритм ранжування PageRank
print 'HITS', nx.hits(G) # алгоритм ранжування HITS повертає вузли, які посилаються на авторитетні вузли і ці авторитетні вузли
