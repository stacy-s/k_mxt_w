import numpy as np
from abc import ABC, abstractmethod


class ClustersData(ABC):
    cluster_numbers = None
    num_of_data = 0
    data_ration = None

    @staticmethod
    def array_rationing(array):
        return (array - np.mean(array)) / np.std(array)

    @abstractmethod
    def distance(self, point: np.ndarray):
        pass

    @abstractmethod
    def get_cluster_name(self, cluster_num):
        if self.cluster_numbers is None:
            raise TypeError('self.cluster_numbers does not equal None')


class MetricsMixin:
    data_ration = None

    # def euclidean_distance(self, point: np.ndarray, start_pos: int, stop_pos: int):
    def euclidean_distance(self, point: np.ndarray):
        return np.sqrt(np.sum((self.data_ration - point) ** 2, axis=1))


class ClustersDataSpace(ClustersData, ABC):
    def __init__(self, x_init: np.ndarray, y_init: np.ndarray):
        if x_init.shape[0] != y_init.shape[0] or len(x_init.shape) != 1 or len(y_init.shape) != 1:
            raise ValueError
        self.x_init = x_init.copy()
        self.y_init = y_init.copy()
        self.data_ration = np.array([ClustersData.array_rationing(self.x_init),
                                     ClustersData.array_rationing(self.y_init)]).transpose()
        self.cluster_numbers = np.full(len(self.x_init), -1)
        self.num_of_data = self.x_init.shape[0]


class ClustersDataSpaceEuclideanEuclidean(MetricsMixin, ClustersDataSpace):
    def __init__(self, x_init: np.ndarray, y_init: np.ndarray):
        super().__init__(x_init, y_init)

    def distance(self, point: np.ndarray):
        return self.euclidean_distance(point)

    def get_cluster_name(self, cluster_num):
        return str(self.cluster_numbers[cluster_num])


