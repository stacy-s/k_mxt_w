import collections
import logging
import time
import numpy as np

import clustering_algorithms
import clustersData
import dataImport
import draw

logger = logging.getLogger('k_mxt_w')


def main():
    print('hello')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler('k_mxt_w.log')
    formatter = logging.Formatter('%(filename)s func:%(funcName)s [LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]' +
                                  '%(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info('Program started')
    try:
        City = collections.namedtuple('City', 'name path_csv latitude longitude')
        cities = {'spb': City(name='spb', path_csv='./datasets/geoflickr_spb.csv',
                              latitude=59.9386300, longitude=30.3141300),
                  'prague': City(name='prague', path_csv='./datasets/geoflickr_prague.csv',
                                 latitude=50.073658, longitude=14.418540)}
        city_key = 'spb'
        data = dataImport.DataImportSpace(filename=cities[city_key].path_csv)
        x, y = data.get_data()
        for k in [3]:
            for eps in np.arange(0.1, 0.5, 0.1):
                clusters_data = clustersData.ClustersDataSpaceEuclidean(x_init=x, y_init=y)
                alg = clustering_algorithms.K_MXT(k=k, eps=eps, clusters_data=clusters_data)
                start_time = time.time()
                alg()
                end_time = time.time()
                print(f'k-{k}, eps-{eps}, time-{end_time - start_time}')
                draw.DrawingClusters.drawing_map(clusters_data,
                                                 f'./results/{cities[city_key].name}/city_{cities[city_key].name}_k_{k}_eps_{eps}',
                                                 cities[city_key].latitude, cities[city_key].longitude, 5)
    except BaseException as e:
        logger.error(e, exc_info=True)
    logger.info('Done!')


if __name__ == '__main__':
    main()
