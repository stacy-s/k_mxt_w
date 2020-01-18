from abc import abstractmethod
import pandas as pd


class DataImport:
    @abstractmethod
    def __init__(self, filename, sep=','):
        self._filename = filename
        self._sep = sep
        self._dataframe = None


class DataImportMixin(object):
    chosen_columns = None

    def read_data(self):
        # self.__dataframe = pd.read_csv(self.__filename, sep=self.__sep)
        # self.__dataframe = self.__dataframe[chosen_columns]
        # self.__dataframe = self.__dataframe.dropna()
        pass


class DataImportSpace(DataImportMixin, DataImport):
    def __init__(self, filename, sep=',', name_col_latitude='latitude', name_col_longitude='longitude'):
        super().__init__(filename=filename, sep=sep)
        self._name_col_latitude = name_col_latitude
        self._name_col_longitude = name_col_longitude
        self.chosen_columns = [self._name_col_latitude, self._name_col_longitude]


class DataImportSpaceDateTime(DataImportSpace):
    def __init__(self, filename, sep=',', name_col_latitude='latitude', name_col_longitude='longitude',
                 name_col_date='datetaken'):
        super().__init__(filename=filename, sep=sep, name_col_latitude=name_col_latitude,
                         name_col_longitude=name_col_longitude)
        self._name_col_date = name_col_date
        self.chosen_columns = [self._name_col_latitude, self._name_col_longitude, self._name_col_date]




