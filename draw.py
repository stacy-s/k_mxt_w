import clustersData
import collections
import random
import matplotlib.pyplot as plt


def rand_color():
    cur_color = hex(random.randint(0, 165))[2:]
    return '0' * (2 - len(cur_color)) + cur_color


class DrawingClusters:
    @classmethod
    def __get_dots_colors(cls, clusters_data, max_noise_size):
        random.seed(10)
        cluster_sizes = collections.Counter(clusters_data.cluster_numbers)
        cluster_colors = dict()
        for key in cluster_sizes:
            if cluster_sizes[key] >= max_noise_size:
                cluster_colors[key] = ''.join(['#', rand_color(), rand_color(), rand_color()])
            else:
                cluster_colors[key] = 'red'
        return [cluster_colors[x] for x in clusters_data.cluster_numbers]

    @classmethod
    def drawing_plot(cls, clusters_data: clustersData.ClustersData, max_noise_size=1):
        color = DrawingClusters.__get_dots_colors(clusters_data, max_noise_size)
        plt.figure(figsize=(35, 35))
        plt.scatter(x=clusters_data.x_init, y=clusters_data.y_init, c=color)
        plt.show()
