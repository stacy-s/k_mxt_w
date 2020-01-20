import ClustersData
from abc import ABC
import numpy as np


class Clustering(ABC):
    def __init__(self, clusters_data: ClustersData.ClustersData):
        self.clustersData = clusters_data


class K_mxt(Clustering):
    def __init__(self, k: int, eps: float, clusters_data: ClustersData.ClustersData):
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
        return np.intersect1d(self.start_graph[v], self.start_graph[to])

    def make_k_graph(self):
        if any(x is None for x in self.start_graph):
            raise TypeError('self.start_graph do not have to consist None.')
        np.random.seed(4000)
        weights_v = []

        def get_k_max_arcs():
            weights = np.array(weight_v, dtype=[('weight', float), ('vertex', int)])
            weights.sort(order='weight')
            weights = np.flip(weights)
            k_value = weights[self.k - 1]
            index_k_value = np.where(weights['weight'] == k_value)[0]
            index_k_value_min, index_k_value_max = index_k_value[0], index_k_value[-1]
            np.random.shuffle(weights[index_k_value_min:index_k_value_max+1])
            return weights['vertex', :self.k]

        for v in range(self.num_of_vertices):
            weight_v = []
            for neighbor in self.start_graph[v]:
                weights_v.append((self.get_arc_weight(v, neighbor), neighbor))
                self.k_graph[v] = get_k_max_arcs()

    def __call__(self, *args, **kwargs):
        self.make_start_graph()
