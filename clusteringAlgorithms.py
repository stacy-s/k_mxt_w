import clustersData
from abc import ABC
import numpy as np
import copy
import graph


class Clustering(ABC):
    def __init__(self, clusters_data: clustersData.ClustersData):
        self.clustersData = copy.deepcopy(clusters_data)


class K_MXT(Clustering):
    def __init__(self, k: int, eps: float, clusters_data: clustersData.ClustersData):
        self.k = k
        self.eps = eps
        self.clusters_data = clusters_data
        self.num_of_vertices = self.clusters_data.num_of_data
        self.start_graph = [None for _ in range(self.num_of_vertices)]
        self.k_graph = [None for _ in range(self.num_of_vertices)]

    def make_start_graph(self):
        for v in range(self.clusters_data.num_of_data):
            dst = self.clusters_data.distance(self.clusters_data.data_ration[v])
            neighbor = np.where(dst <= self.eps)[0]
            index_v = np.argwhere(neighbor == v)
            neighbor = np.delete(neighbor, index_v)
            self.start_graph[v] = neighbor

    def get_arc_weight(self, v, to):
        return np.intersect1d(self.start_graph[v], self.start_graph[to]).shape[0]

    def make_k_graph(self):
        if any(x is None for x in self.start_graph):
            raise TypeError('self.start_graph do not have to consist None.')
        np.random.seed(4000)
        weights_v = []

        def get_k_max_arcs():
            weights = np.array(weights_v, dtype=[('weight', float), ('vertex', int)])
            if weights.shape[0] < self.k:
                return weights['vertex']
            weights.sort(order='weight')
            weights = np.flip(weights)
            k_value = weights['weight'][self.k - 1]
            index_k_value = np.where(weights['weight'] == k_value)[0]
            index_k_value_min, index_k_value_max = index_k_value[0], index_k_value[-1]
            np.random.shuffle(weights[index_k_value_min:index_k_value_max+1])
            return weights['vertex'][:self.k]

        for v in range(self.num_of_vertices):
            weights_v = []
            for neighbor in self.start_graph[v]:
                weights_v.append((self.get_arc_weight(v, neighbor), neighbor))
            self.k_graph[v] = get_k_max_arcs()

    def __call__(self, *args, **kwargs):
        self.make_start_graph()
        self.make_k_graph()
        g = graph.Graph(adj=self.k_graph)
        self.clusters_data.cluster_numbers = g.find_scc()

