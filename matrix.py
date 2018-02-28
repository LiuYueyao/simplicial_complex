#!usr/bin/env python3
# coding: utf-8

from numpy import *
import numpy as np
import read_file
import time

def main():
    # node_list = [[0,1,1,1,0,0,0,0,0],
    #             [0,0,1,1,0,0,0,0,0],
    #             [0,0,0,1,1,0,0,0,0],
    #             [0,0,0,0,1,1,0,0,0],
    #             [0,0,0,0,0,1,0,0,0],
    #             [0,0,0,0,0,0,1,1,1],
    #             [0,0,0,0,0,0,0,1,0],
    #             [0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0]]
    # node_adj_mat = mat(node_list)
    # node_adj_mat += node_adj_mat.T
    #
    # n_node = len(node_list)
    # node_name_list = [set([i+1]) for i in range(n_node)] # name of nodes

    node_adj_mat = read_file.net_mat
    node_adj_mat += node_adj_mat.T
    node_name_list = read_file.name_list
    n_node = read_file.n_node

    # edge_name_list
    edge_name_list = []
    for i in range(n_node):
        for j in range(i+1, n_node):
            if node_adj_mat[i,j] == 1:
                edge_name_list.append(node_name_list[i]|node_name_list[j]) #set union

    n_edge = len(edge_name_list)
    edge_lower_mat = mat([[0]*n_edge]*n_edge)
    edge_upper_mat = mat([[0]*n_edge]*n_edge)
    edge_dimension = 1

    tri_name_list = []
    for i in range(n_edge):
        for j in range(i+1, n_edge):
            # lower
            if len(edge_name_list[i] & edge_name_list[j]) == edge_dimension:
                edge_lower_mat[i,j] = 1
            # upper
            tmp_set = (edge_name_list[i]|edge_name_list[j]) - (edge_name_list[i] & edge_name_list[j])
            if tmp_set in edge_name_list:
                edge_upper_mat[i,j] = 1
                tri_name_list.append(tuple(edge_name_list[i] | edge_name_list[j]))

    edge_lower_mat += edge_lower_mat.T
    edge_upper_mat += edge_upper_mat.T
    # edge_adj_mat
    edge_adj_mat = edge_lower_mat - edge_upper_mat


    # triangle
    tri_name_list = [set(s) for s in set(tri_name_list)]
    n_tri = len(tri_name_list)
    tri_dimension = 2
    tri_lower_mat = mat([[0]*n_tri]*n_tri)
    tri_upper_mat = mat([[0]*n_tri]*n_tri)
    for i in range(n_tri):
        for j in range(i+1, n_tri):
            if len(tri_name_list[i] & tri_name_list[j]) == tri_dimension:
                tri_lower_mat[i,j] = 1

            tmp_set = (tri_name_list[i]|tri_name_list[j]) - (tri_name_list[i] & tri_name_list[j])
            if tmp_set in edge_name_list:
                tri_upper_mat[i,j] = 1

    tri_lower_mat += tri_lower_mat.T
    tri_upper_mat += tri_upper_mat.T
    tri_adj_mat = tri_lower_mat - tri_upper_mat


    # all adjacency matrix
    print("n_node: ", n_node)
    # print(node_name_list)
    # print(node_adj_mat)

    print("n_edge: ", n_edge)
    # print(edge_name_list)
    # print(edge_adj_mat)

    print("n_tri: ", n_tri)
    # print(tri_name_list)
    # print(tri_adj_mat)


if __name__ == '__main__':
    start_time = time.clock()
    main()
    print("time:", time.clock()-start_time)