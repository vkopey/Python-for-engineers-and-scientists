# -*- coding: utf-8 -*-
"""
# NetworkX - графи
NetworkX (http://networkx.github.io) - це пакет для створення, маніпуляції і вивчення структури, динаміки і функціонування комплексних графів. Граф - це абстрактний математичний об'єкт, який являє собою множину вершин і ребер, які з'єднують пари вершин. В прикладі показані основи створення і використання неорієнтованих графів за допомогою NetworkX 2.0.
"""
import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph() # створити неорієнтований граф
G.add_node(1) # додати вузол
G.add_node('A') # додати вузол (вузлом може бути будь-який об'єкт)
G.add_nodes_from([2,3,4]) # додати вузли
G.add_edge(1,2) # додати ребро
G.add_edges_from([(2,3),(3,4),(4,2),(2,'A')]) # додати ребра

print G.number_of_nodes(), G.number_of_edges() # кількість вузлів і ребер
print 'nodes', G.nodes # вузли
print 'edges', G.edges # ребра
print 'adj', G.adj # сусіди вершин
print 'degree', G.degree # степені вершин (кількість ребер вершин)

print G.edges(['A',2,3]) # усі ребра вершин 'A',2,3
print G[2] # сусіди вершини 2, або G.adj[2]
print G.degree(['A',2,3]) # степені вершин 'A',2,3

G.node['A']['a']="val1" # змінити значення атрибута 'a' вузла 'A'
print G.nodes['A'] # словник атрибутів вузла

G[1][2]["color"]="blue" # змінити значення атрибута 'color' ребра 1,2
# або G.edges[1,2]["color"]="blue"
G[1][2]['weight'] = 4 # спеціальний атрибут зважених графів
print G[1][2] # словник атрибутів ребра 1,2

# ітерація по кортежам (node, neighbors), де neighbors - словник:
for node, neighbors in G.adj.items():
    print "Сусіди вузла", node
    for neighbor, edge_attr in neighbors.items(): # для кожного сусіда
        print '    ', neighbor, edge_attr # сусід, властивості ребра

#nx.draw(G, with_labels = True) # рисувати граф за допомогою matplotlib
nx.draw_circular(G, with_labels = True) # інші способи візуалізації графа
#nx.draw_spectral(G, with_labels = True)
plt.show(); print "Рисунок - Візуалізація графа"

#якщо Graphviz і PyGraphviz (nx_agraph) або pydot (nx_pydot) установлені, то можна рисувати, зберігати і читати граф у форматі dot. Підтримуються також інші формати.
#nx.draw(G, pos=nx.nx_agraph.graphviz_layout(G)) # рисувати
#nx.drawing.nx_agraph.write_dot(G, "myGraph.dot") # зберегти
#G=nx.drawing.nx_agraph.read_dot("myGraph.dot") # прочитати