import copy
import numpy as np


class Graph:
    def __init__(self, adj):
        self.adj = copy.deepcopy(adj)
        self.num_vertices = len(self.g)

    def get_reverse_graph(self):
        adj = [[] for _ in range(self.num_vertices)]
        for v in range(self.num_vertices):
            for to in self.adj[v]:
                adj[to].append(v)
        return Graph(adj=adj)

    def dfs(self, vertex_order, is_save_processing_order):
        num_ucc = [0 for _ in range(self.num_vertices)]
        processing_order = None
        if is_save_processing_order:
            processing_order = []

        def dfs(s):
            num_ucc[s] = cnt_call
            for neighbor in self.adj[s]:
                if not num_ucc[neighbor]:
                    dfs(neighbor)
            if is_save_processing_order:
                processing_order.append(s)

        cnt_call = 0
        for v in vertex_order:
            if not num_ucc[v]:
                cnt_call += 1
                dfs(v)
        if is_save_processing_order:
            return num_ucc, processing_order
        return num_ucc

    def run_dfs(self):
        vertex_order = [x for x in range(self.num_vertices)]
        return self.dfs(vertex_order=vertex_order, is_save_processing_order=False)

    def top_sort(self):
        vertex_order = [x for x in range(self.num_vertices)]
        order_top_sort = self.dfs(vertex_order=vertex_order, is_save_processing_order=True)[1]
        order_top_sort.reverse()
        return order_top_sort

    def find_scc(self):
        g_rev = self.get_reverse_graph()
        order = g_rev.top_sort()
        return self.dfs(vertex_order=order, is_save_processing_order=False)






