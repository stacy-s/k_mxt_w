import collections
import logging
import time
import numpy as np

import clustering_algorithms
import clustersData
import data_import
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
        sf_filename = '../data/sanfranciso-crime-dataset/Police_Department_Incidents_-_Previous_Year__2016_.csv'
        data = data_import.DataCrimeImportSpace(filename=sf_filename)
        name_crime_col = 'Category'
        need_values = ['STOLEN PROPERTY']
        data.filter_type_crime(name_crime_col, need_values)
        latitude, longitude = (37.7749300, -122.4194200)
        x, y = data.get_data(name_location_col='Location')
        print(len(x))
        for k in [3]:
            for eps in [0.2]:
                clusters_data = clustersData.ClustersDataSpaceEuclidean(x_init=x, y_init=y)
                alg = clustering_algorithms.K_MXT(k=k, eps=eps, clusters_data=clusters_data)
                start_time = time.time()
                # alg()
                end_time = time.time()
                print(f'k-{k}, eps-{eps}, time-{end_time - start_time}')
                need_values_for_path = [s.replace("/", "-") for s in need_values]
                draw.DrawingClusters.drawing_map(clusters_data,
                                                 f'./results/crimes_sf_{need_values_for_path}_k_{k}_eps_{eps}',
                                                 city_lat=latitude, city_long=longitude, max_noise_size=0)
    except BaseException as e:
        logger.error(e, exc_info=True)
    logger.info('Done!')


if __name__ == '__main__':
    main()
