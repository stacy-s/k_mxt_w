import logging
import time
import numpy as np
import os

import clustering_algorithms
import clusters_data
import data
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
    # try:
    filename = '../data/homegate_month_living_dropna.csv'
    data_property = data.DataPropertyImportSpace(filename=filename)

    features_list = ['price']
    x, y, features = data_property.get_data(features_list=features_list)
    for k in [15]:
        for eps in [0.1]:
            clusters = clusters_data.ClustersDataSpaceFeaturesEuclidean(x_init=x, y_init=y, features_init=features)
            alg = clustering_algorithms.K_MXT(k=k, eps=eps, clusters_data=clusters)
            start_time = time.time()
            alg()
            end_time = time.time()
            print(f'k-{k}, eps-{eps}, time-{end_time - start_time}')
            clusters.cluster_numbers = clusters.cluster_numbers.reshape(-1, 1)
            data.DataSave.arrays_to_csv(new_filename=f'./results/{os.path.basename(filename)}_k_{k}_eps_{eps}.csv',
                                        lalitude=x, longitude=y, price=features,
                                        cluster_numbers=clusters.cluster_numbers,
                                        )
    draw.Draw.draw_points(filename=filename, lat='latitude', lon='longitude', hover_name='price',
                          hover_data=['rooms', 'url', 'property_type'],
                          color='price')
    # draw.Draw.draw_points(filename=filename, lat='latitude', lon='longitude',
    #                       hover_name='rent_per_room',
    #                       hover_data=['price', 'rooms'],
    #                       color='rent_per_room',
    #                       )

    # except BaseException as e:
    #     logger.error(e, exc_info=True)
    # logger.info('Done!')


if __name__ == '__main__':
    main()
