import pandas as pd
import os


class loader:
    def __init__(self,):
        _path = os.path.join(os.path.dirname(__file__))
        file_path = os.path.join(_path, "resources/country-codes.csv")
        self.data = pd.read_csv(file_path)

    def __get__(self, instance, owner):
        return self.data

    def __set__(self, instance, value):
        raise AttributeError(f'cannot set attribute to {value}')

    def copy(self):
        return self.data.copy()


class Columns:
    _raw_data = loader()
    data = _raw_data.copy()

    def __init__(self, ):
        self.all_columns = self.data.columns

    @property
    def idle_columns(self):
        cols = [
                    'UNTERM Arabic Formal',
                    'UNTERM Chinese Short official_name_ar',
                    'UNTERM Russian Short',
                    'UNTERM Chinese Formal',
                    'UNTERM French Formal',
                    'UNTERM Spanish Short',
                    'UNTERM Russian Formal',
                    'official_name_fr',
                    'UNTERM French Short',
                    'UNTERM Spanish Formal',
                    'UNTERM French Formal',
                    'UNTERM Chinese Short',
                    'official_name_ru',
                    'UNTERM Spanish Short',
                    'UNTERM Arabic Short',
                    'official_name_ar',
                    'official_name_es',
                    'official_name_cn'
                    ]
        return cols

    @property
    def active_columns(self):
        return [i for i in self.all_columns if i not in self.idle_columns]

    @property
    def country_name_columns(self):
        cols = [
            'ISO3166-1-Alpha-3',
            'ISO3166-1-Alpha-2',
            'UNTERM English Short',
            'UNTERM English Formal',
            'official_name_en',
            "CLDR display name",
            'Geoname ID',
            'Least Developed Countries (LDC)',
            'Land Locked Developing Countries (LLDC)',
            'ISO4217-currency_name',
            'ISO4217-currency_alphabetic_code',
            'Continent',
        ]
        return cols

    @property
    def column_str_types(self):
        return {item: str for item in self.country_name_columns}

    @property
    def rename_cols(self):
        # 'FIFA','GAUL','FIPS','WMO','MARC','ITU','IOC','DS','M49','TLD','EDGAR'
        rename = {
                    'Dial': "dial",
                    'ISO3166-1-Alpha-3': "ISO3166_1_Alpha_3",
                    'ISO3166-1-numeric': "ISO3166_1_numeric",
                    'ISO3166-1-Alpha-2': "ISO3166_1_Alpha_2",
                    'Global Code': "global_code",
                    'Intermediate Region Code': "intermediate_region_code",
                    'ISO4217-currency_name': "ISO4217_currency_name",
                    'Developed / Developing Countries': "development_status",
                    'UNTERM English Short': "english_short_name",
                    'ISO4217-currency_alphabetic_code': "ISO4217_currency_alphabetic_code",
                    'Small Island Developing States (SIDS)': "",
                    'ISO4217-currency_numeric_code': "ISO4217_currency_numeric_cod",
                    'Sub-region Code': "subregion_code",
                    'Region Code': "region_code",
                    'ISO4217-currency_minor_unit': "ISO4217_currency_minor_unit",
                    'Land Locked Developing Countries (LLDC)': "is_land_locked_dev_country",
                    'Intermediate Region Name': "intermediate_region_name",
                    'UNTERM English Formal': "english_formal_name",
                    'official_name_en': "official_name",
                    'ISO4217-currency_country_name': "ISO4217_currency_country_name",
                    'Least Developed Countries (LDC)': "is_least_developed",
                    'Region Name': "region_name",
                    'Sub-region Name': "sub_region_name",
                    'Global Name': "global_name",
                    'Capital': "capital",
                    'Continent': "continent",
                    'Languages': "languages",
                    'Geoname ID': "geoname_ID",
                    'CLDR display name': "CLDR_display_name",
        }
        return rename
