from abc import abstractmethod
import pandas as pd
import datetime


class DataImport:
    @abstractmethod
    def __init__(self, filename, sep=','):
        self._filename = filename
        self._sep = sep
        self._dataframe = None


class DataImportMixin(object):
    chosen_columns = None

    def _read_data(self):
        self._dataframe = pd.read_csv(self._filename, sep=self._sep)
        self._dataframe = self._dataframe[self.chosen_columns]
        self._dataframe = self._dataframe.dropna()
        self._dataframe = self._dataframe[self.chosen_columns].drop_duplicates(keep='first')


class DataImportSpace(DataImportMixin, DataImport):
    def __init__(self, filename, sep=',', name_col_x='latitude', name_col_y='longitude',
                 name_col_date='datetaken', name_col_owner='owner'):
        super().__init__(filename=filename, sep=sep)
        self._name_col_x = name_col_x
        self._name_col_y = name_col_y
        self._name_col_date = name_col_date
        self._name_col_owner = name_col_owner
        self.chosen_columns = [self._name_col_x, self._name_col_y, self._name_col_date, self._name_col_owner]

    def get_data(self):
        self._read_data()
        return self._dataframe[self._name_col_x].to_list(), self._dataframe[self._name_col_y].to_list()


class DataImportSpaceDateTime(DataImportSpace):
    def __init__(self, filename, sep=',', name_col_x='latitude', name_col_y='longitude',
                 name_col_date='datetaken', name_col_owner='owner'):
        super().__init__(filename=filename, sep=sep, name_col_x=name_col_x,
                         name_col_y=name_col_y, name_col_date=name_col_date, name_col_owner=name_col_owner)

    def get_data(self):
        x, y = super().get_data()
        return x, y, [dt.to_pydatetime() for dt in pd.to_datetime(self._dataframe[self._name_col_date])]




