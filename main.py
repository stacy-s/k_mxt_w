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
        #   filename = '../data/AB_NYC_2019.csv'
        filename = '../data/Airbnb_Texas_Rentals_dropna.csv'
        data = data_import.DataAirbnbImportSpace(filename=filename)
        #     latitude, longitude = (40.730610, -73.935242)
        latitude, longitude = (29.3838500, -94.9027000)

        features_list = ['price']
        x, y, features = data.get_data(features_list=features_list)
        print(len(x))
        for k in [15]:
            for eps in [0.1]:
                print(x, y, features)
                clusters = clusters_data.ClustersDataSpaceFeaturesEuclidean(x_init=x, y_init=y, features_init=features)
                alg = clustering_algorithms.K_MXT(k=k, eps=eps, clusters_data=clusters)
                start_time = time.time()
                alg()
                end_time = time.time()
                print(f'k-{k}, eps-{eps}, time-{end_time - start_time}')
                draw.DrawingClusters.drawing_map(clusters,
                                                 f'./results/airbnb_texas_gauss_k_{k}_eps_{eps}',
                                                 city_lat=latitude, city_long=longitude, max_noise_size=1)
    except BaseException as e:
        logger.error(e, exc_info=True)
    logger.info('Done!')


if __name__ == '__main__':
    main()
