import logging
import time
import numpy as np

import clustering_algorithms
import clusters_data
import data_import
import draw

logger = logging.getLogger('k_mxt_w')


def main():
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler('k_mxt_w.log')
    formatter = logging.Formatter('%(filename)s func:%(funcName)s [LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]' +
                                  '%(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info('Program started')
    try:
        sf_filename = '../data/AB_NYC_2019.csv'
        data = data_import.DataAirbnbImportSpace(filename=sf_filename)
        latitude, longitude = (40.730610, -73.935242)
        features_list = ['price']
        x, y, features = data.get_data(features_list=features_list)
        print(len(x))
        for k in [3]:
            for eps in [0.2]:
                print(x, y, features)
                clusters = clusters_data.ClustersDataSpaceFeaturesEuclidean(x_init=x, y_init=y, features_init=features)
                alg = clustering_algorithms.K_MXT(k=k, eps=eps, clusters_data=clusters)
                start_time = time.time()
                alg()
                end_time = time.time()
                print(f'k-{k}, eps-{eps}, time-{end_time - start_time}')
                print(clusters.cluster_numbers)
                # draw.DrawingClusters.drawing_map(clusters_data,
                #                                  f'./results/airbnb_ny_k_{k}_eps_{eps}',
                #                                  city_lat=latitude, city_long=longitude, max_noise_size=0, color=data._dataframe[data._dataframe['price']<2000]['price'] // 8)
    except BaseException as e:
        logger.error(e, exc_info=True)
    logger.info('Done!')


if __name__ == '__main__':
    main()
