import clustersData
import collections
import random
import matplotlib as plt


def rand_color():
    cur_color = hex(random.randint(0, 165))[2:]
    return '0' * (2 - len(cur_color)) + cur_color


class drawing_clusters:
    cluster_colors = dict()
    cluster_sizes = None
    noise_color = '#FF0000'
    max_noise_size = 1
    clusters_data = None

    @classmethod
    def __make_dots_colors(self):
        random.seed(10)
        self.cluster_sizes = collections.Counter(self.clusters_data.cluster_numbers)
        print(self.cluster_sizes)
        for key, value in self.cluster_colors:
            if value <= self.max_noise_size:
                self.cluster_colors[key] = ''.join(['#', rand_color(), rand_color(), rand_color()])

    @classmethod
    def drawing_plot(self, clusters_data: clustersData.ClustersData, max_noise_size=1):
        self.clusters_data = clusters_data
        self.max_noise_size = max_noise_size
        self.__make_dots_colors()
        print(self.clusters_data.cluster_numbers, self.cluster_colors)
        color = [self.cluster_colors[x] for x in self.clusters_data.cluster_numbers]
        plt.figure(figsize=(25, 25))
        plt.scatter(x=self.clusters_data.x_init, y=self.clusters_data.y_init, c=color)
        plt.show()
