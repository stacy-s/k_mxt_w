from abc import abstractmethod, ABC
import pandas as pd
import datetime
import numpy as np
import re
import logging


logger = logging.getLogger('k_mxt_w.data_import')


class DataImport(ABC):
    _dataframe = None

    @abstractmethod
    def __init__(self, filename, sep=','):
        self._filename = filename
        self._sep = sep


class DataImportMixin:
    chosen_columns = None

    def _read_data(self):
        self._dataframe = pd.read_csv(self._filename, sep=self._sep, low_memory=False)


class DataCrimeImportSpace(DataImportMixin, DataImport):
    def __init__(self, filename, sep=','):
        super().__init__(filename, sep)
        logger.info(f'filename-{self._filename}, sep-{sep}')
        self._read_data()

    def filter_type_crime(self, name_type_crime_col, need_values):
        self._dataframe = self._dataframe[self._dataframe[name_type_crime_col].isin(need_values)]

    def get_data(self, name_location_col):
        coordinates = self._dataframe[name_location_col].map(lambda x: re.split(
            r'[,]',
            re.sub(r'[()]', '', x)
        ))
        x = coordinates.map(lambda x: x[0])
        y = coordinates.map(lambda x: x[1])
        return x.to_numpy(), y.to_numpy()


class DataAirbnbImportSpace(DataImportMixin, DataImport):
    def __init__(self, filename, sep=','):
        super().__init__(filename, sep)
        logger.info(f'filename-{self._filename}, sep-{sep}')
        self._read_data()

    def get_data(self, name_latitude_cols='latitude', name_longitude_cols='longitude', features_list=None):
        x = self._dataframe[name_latitude_cols].to_numpy(dtype=np.float)
        y = self._dataframe[name_longitude_cols].to_numpy(dtype=np.float)
        return x, y, self._dataframe[features_list].to_numpy(dtype=np.float)


# class DataAirbnbImportSpaceFeatures(DataAirbnbImportSpace):
#     def  __init__(self, filename, features_list, sep=','):
#         super().__init__(filename, sep)
#         self.features_list = features_list
#         self.features = self._dataframe[features_list].to_numpy()

#
#
#
# class DataImportSpace(DataImportMixin, DataImport):
#     def __init__(self, filename, sep=',', name_col_x='latitude', name_col_y='longitude',
#                  name_col_date='datetaken', name_col_owner='owner'):
#         super().__init__(filename=filename, sep=sep)
#         self._name_col_x = name_col_x
#         self._name_col_y = name_col_y
#         self._name_col_date = name_col_date
#         self._name_col_owner = name_col_owner
#         self.chosen_columns = [self._name_col_x, self._name_col_y, self._name_col_date, self._name_col_owner]
#
#     def get_data(self):
#         self._read_data()
#         return self._dataframe[self._name_col_x].to_numpy(), self._dataframe[self._name_col_y].to_numpy()
#
#
# class DataCrimesImportSpace(DataImportSpace):
#     def __init__(self, filename, sep=',', name_col_x='latitude', name_col_y='longitude',
#                  name_col_date='datetaken', name_col_owner='owner'):
#         super.__init__(filename, sep, name_col_x, name_col_y, name_col_date, name_col_owner)
#
#
#
# class DataImportSpaceTime(DataImportSpace):
#     def __init__(self, filename, sep=',', name_col_x='latitude', name_col_y='longitude',
#                  name_col_date='datetaken', name_col_owner='owner'):
#         super().__init__(filename=filename, sep=sep, name_col_x=name_col_x,
#                          name_col_y=name_col_y, name_col_date=name_col_date, name_col_owner=name_col_owner)
#
#     def get_data(self):
#         x, y = super().get_data()
#         return x, y, pd.to_datetime(self._dataframe[self._name_col_date]).map(lambda x: x.time()).to_numpy()
#
#
# class DataImportSpaceDateTime(DataImportSpace):
#     def __init__(self, filename, sep=',', name_col_x='latitude', name_col_y='longitude',
#                  name_col_date='datetaken', name_col_owner='owner'):
#         super().__init__(filename=filename, sep=sep, name_col_x=name_col_x,
#                          name_col_y=name_col_y, name_col_date=name_col_date, name_col_owner=name_col_owner)
#
#     def get_data(self):
#         x, y = super().get_data()
#         return x, y, np.array([dt.to_pydatetime() for dt in pd.to_datetime(self._dataframe[self._name_col_date])])
