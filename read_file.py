#!usr/bin/env python3
# coding: utf-8

import re
from numpy import *
import numpy as np

name_list = []
vertex_flag = False
edge_flag = False
with open('data/YeastS.net') as net_file:
    for line in net_file:
        if line.startswith('%'):
            continue

        if line.startswith('*vertices'):
            vn = re.search('\d+',line)
            n_node = int(vn.group())
            net_mat = mat([[0]*n_node]*n_node)
            vertex_flag = True
            edge_flag = False
        elif line.startswith('*edges'):
            edge_flag = True
            vertex_flag = False

        else:
            if vertex_flag:
                name_match = re.search('(\d+)\s+\"(.*)\"', line)
                name_list.append(set([name_match.group(2)]))
            elif edge_flag:
                edge_match = re.search('(\d+)\s+(\d+)',line)
                net_mat[int(edge_match.group(1))-1, int(edge_match.group(2))-1] = 1
