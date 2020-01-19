import numpy as np


class ClustersData:
    @staticmethod
    def array_rationing(array):
        return (array - np.mean(array)) / np.std(array)


class SpaceMetricsMixin:
    data_ration = None

    # def euclidean_distance(self, point: np.ndarray, start_pos: int, stop_pos: int):
    def euclidean_distance(self, point: np.ndarray):
        return np.sqrt(np.sum((self.data_ration - point) ** 2, axis=1))


class ClustersDataSpace(ClustersData):
    def __init__(self, x_init: np.ndarray, y_init: np.ndarray):
        self.x_init = x_init.copy()
        self.y_init = y_init.copy()
        self.data_ration = np.array([ClustersData.array_rationing(self.x_init),
                                     ClustersData.array_rationing(self.y_init)]).transpose()


class ClustersDataSpaceEuclidean(SpaceMetricsMixin, ClustersDataSpace):
    def __init__(self, x_init: np.ndarray, y_init: np.ndarray):
        super().__init__(x_init, y_init)

