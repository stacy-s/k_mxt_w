import numpy as np
from abc import ABC, abstractmethod
import datetime


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
    time_init = None

    # def euclidean_distance(self, point: np.ndarray, start_pos: int, stop_pos: int):
    def euclidean_distance(self, num_point):
        return np.sqrt(np.sum((self.data_ration - self.data_ration[num_point]) ** 2, axis=1))

    def euclidean_distance(self, point1, point2):
        return np.sqrt(np.sum((self.data_ration[point1] - self.data_ration[point2]) ** 2, axis=1))

    def euclidean_distance_according_time(self, num_point):
        distance = np.sqrt(np.sum((self.data_ration[:, :2] - self.data_ration[num_point][:2]) ** 2, axis=1))
        return


    # def euclidean_distance_dependent_on_time(self, num_point):
    #     dst = self.euclidean_distance(num_point)
    #     INF = 1e9
    #     subtraction_time = []
    #     max_subtraction = datetime.timedelta(hour=3)
    #     for d in dst:
    #         if abs(d - self.time_init) > max_subtraction:
    #             subtraction_time.append(INF)
    #         else:
    #             subtraction_time.append(d)


class ClustersDataSpace(ClustersData, ABC):
    def __init__(self, x_init: np.ndarray, y_init: np.ndarray):
        if x_init.shape != y_init.shape:
            raise ValueError('x_init and y_init must be the same dimension')
        self.x_init = x_init.copy()
        self.y_init = y_init.copy()
        self.data_ration = None
        self.cluster_numbers = np.full(len(self.x_init), -1)
        self.num_of_data = self.x_init.shape[0]


class ClustersDataSpaceEuclidean(MetricsMixin, ClustersDataSpace):
    def __init__(self, x_init: np.ndarray, y_init: np.ndarray):
        super().__init__(x_init, y_init)
        self.data_ration = np.array([self.x_init,
                                     self.y_init]).transpose()

    def distance(self, point):
        return self.euclidean_distance(point)

    def distance(self, point1, point2):
        return self.euclidean_distance(point1, point2)

    def get_cluster_name(self, cluster_num):
        super().get_cluster_name(cluster_num)
        return str(cluster_num)


class ClustersDataSpaceFeatures(ClustersDataSpace, ABC):
    def __init__(self, x_init: np.ndarray, y_init: np.ndarray, features_init: np.ndarray):
        """
        :param x_init:
        :param y_init:
        :param features_init: each row corresponds to a single data point.
        """
        super().__init__(x_init, y_init)
        self.features_init = features_init.copy()
        self.data_ration = np.array([ClustersData.array_rationing(self.x_init),
                                             super().array_rationing(self.y_init),
                                             super().array_rationing(self.time_init)]).transpose()


class ClustersDataSpaceFeatures(ClustersDataSpace, ABC):
    def __init__(self, x_init: np.ndarray, y_init: np.ndarray, features_init: np.ndarray):
        super().__init__(x_init, y_init, features_init)

    def distance(self, point):
        return self.euclidean_distance(point)

    def distance(self, point1, point2):
        return self.euclidean_distance(point1, point2)



#
# class ClustersDataSpaceTime(ClustersDataSpace, ABC):
#     def __init__(self, x_init: np.ndarray, y_init: np.ndarray, time_init: np.ndarray):
#         super().__init__(x_init, y_init)
#         if x_init.shape != time_init.shape:
#             raise ValueError('x_init and time_init must be the same dimension')
#         self.time_init = time_init.copy()
#         self.data_ration = np.array([ClustersData.array_rationing(self.x_init),
#                                      ClustersData.array_rationing(self.y_init),
#                                      ClustersDataSpaceTime._array_rationing_time(self.time_init)]).transpose()
#
#     @staticmethod
#     def _array_rationing_time(array):
#         time = np.array(
#             [datetime.timedelta(hours=x.hour, minutes=x.minute, seconds=x.second).total_seconds() for x in array]
#         )
#         return ClustersData.array_rationing(time)
#
#     def get_cluster_name(self, cluster_num):
#         times = [self.time_init[i] for i, x in enumerate(self.cluster_numbers) if x == cluster_num]
#         min_time = str(min(times))
#         max_time = str(max(times))
#         return ' '.join([str(self.cluster_numbers[cluster_num]), min_time, max_time])

#
# class ClustersDataSpaceTimeEuclidean(MetricsMixin, ClustersDataSpaceTime):
#     def __init__(self, x_init: np.ndarray, y_init: np.ndarray, time_init: np.ndarray):
#         super().__init__(x_init, y_init, time_init)
#
#     def distance(self, point: np.ndarray):
#         return self.euclidean_distance(point)
