#!usr/bin/env python3
# coding: utf-8

from numpy import *
import numpy as np
import matrix

# degree centrality
node_degree_list = [sum(node_adj_mat[i]) for i in range(n_node)]
node_name_list_ct = [tuple(s) for s in node_name_list]  # copy tuple
node_degree_dict = dict(zip(node_name_list_ct,node_degree_list))
print(sorted(node_degree_dict.items(),key=lambda item:item[1], reverse=True))


edge_degree_list = [sum(edge_adj_mat[i]) for i in range(n_edge)]
edge_name_list_ct = [tuple(s) for s in edge_name_list]  # copy tuple
edge_degree_dict = dict(zip(edge_name_list_ct,edge_degree_list))
# print(sorted(edge_degree_dict.items(),key=lambda item:item[1], reverse=True))

vertex_edge_degree_dict = dict(zip(node_name_list_ct, [0]*n_node))
vertex_inv_count_dict = dict(zip(node_name_list_ct, [0]*n_node))

for i in edge_degree_dict.items():  # i[0] = key, i[1] = value  key is a tuple
    for v in i[0]:
        vertex_edge_degree_dict[(v,)] += i[1]
        vertex_inv_count_dict[(v,)] += 1

for i in vertex_edge_degree_dict.keys():
    if vertex_inv_count_dict[i]:
        vertex_edge_degree_dict[i] /= vertex_inv_count_dict[i]

print(sorted(vertex_edge_degree_dict.items(),key=lambda item:item[1], reverse=True))


tri_degree_list = [sum(tri_adj_mat[i]) for i in range(n_tri)]
tri_name_list_ct = [tuple(s) for s in tri_name_list]  # copy tuple
tri_degree_dict = dict(zip(tri_name_list_ct,tri_degree_list))
# print(sorted(tri_degree_dict.items(),key=lambda item:item[1], reverse=True))


vertex_tri_degree_dict = dict(zip(node_name_list_ct, [0]*n_node))
vertex_inv_count_dict = dict(zip(node_name_list_ct, [0]*n_node))

for i in tri_degree_dict.items():  # i[0] = key, i[1] = value  key is a tuple
    for v in i[0]:
        vertex_tri_degree_dict[(v,)] += i[1]
        vertex_inv_count_dict[(v,)] += 1

for i in vertex_tri_degree_dict.keys():
    if vertex_inv_count_dict[i]:
        vertex_tri_degree_dict[i] /= vertex_inv_count_dict[i]

print(sorted(vertex_tri_degree_dict.items(),key=lambda item:item[1], reverse=True))
