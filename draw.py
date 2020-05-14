import clusters_data
import collections
import random
import matplotlib.pyplot as plt
import folium


Point = collections.namedtuple('Point', ['x', 'y'])

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
    def drawing_plot(cls, clusters_data: clusters_data.ClustersData, max_noise_size=1):
        color = DrawingClusters.__get_dots_colors(clusters_data, max_noise_size)
        plt.figure(figsize=(35, 35))
        plt.scatter(x=clusters_data.x_init, y=clusters_data.y_init, c=color)
        plt.show()

    @classmethod
    def drawing_map(cls, clusters_data: clusters_data.ClustersData, filename, city_lat, city_long, max_noise_size=1, color=None):
        # color = DrawingClusters.__get_dots_colors(clusters_data, max_noise_size)
        color = [f'#{c}{c}{c}' for c in color.to_numpy()]
        fmap = folium.Map([city_lat, city_long])
        folium.TileLayer(
            tiles='https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_nolabels/{z}/{x}/{y}{r}.png',
            attr='My').add_to(fmap)
        folium.TileLayer(
            tiles='https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager_nolabels/{z}/{x}/{y}{r}.png',
            attr='My').add_to(fmap)
        folium.LayerControl().add_to(fmap)
        for i in range(clusters_data.num_of_data):
            folium.CircleMarker([clusters_data.x_init[i], clusters_data.y_init[i]],
                                radius=1, fill=True, color=color[i],
                                popup=clusters_data.get_cluster_name(clusters_data.cluster_numbers[i])).add_to(fmap)
        fmap.save(filename + '.html')
