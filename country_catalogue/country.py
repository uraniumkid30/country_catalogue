from types import SimpleNamespace
from .columns import Columns
from .utils import Private


class CountryData:
    def __init__(self, country_info):
        for key in country_info:
            setattr(self, key, country_info[key])

    def __str__(self):
        return f"{self.official_name} ({self.ISO3166_1_Alpha_3})"


class SimpleJsonspace(SimpleNamespace):
    def __repr__(self):
        return f"{self.official_name} ({self.ISO3166_1_Alpha_3})"


@Private('data')
class CountryCatalogue(Columns):
    def __init__(self):
        Columns.__init__(self)
        self.data = self.data.astype(self.column_str_types)
        self._clean_df()
        self.continents = {
            "asia": "AS",
            "africa": "AF",
            "northamerica": "NA",
            "southamerica": "SA",
            "oceania": "OC",
            "antarctica": "AN",
            "europe": "EU",
        }

    def _clean_df(self):
        conversions = [lambda x: False if x == 'nan' else True]
        conversions.append(lambda x: x.replace(" ", "_").lower())
        bool_cols = ['Least Developed Countries (LDC)', 'Land Locked Developing Countries (LLDC)']
        lower_cols = [
            'CLDR display name',
            'UNTERM English Formal',
            'official_name_en',
            'ISO4217-currency_name'
        ]
        for i in bool_cols:
            self.data[i] = self.data[i].apply(conversions[0])
        for i in lower_cols:
            self.data[i] = self.data[i].apply(conversions[1])

    def get_country_info(*self, **kwargs):
        self = self[0]
        required = ["alpha_2", "alpha_3", "name", "geoname_id"]
        alpha2 = kwargs.get("alpha_2")
        alpha3 = kwargs.get("alpha_3")
        country_name = kwargs.get("name")
        geoname_id = kwargs.get("geoname_id")
        if all(x is None for x in {alpha2, alpha3, country_name, geoname_id}):
            raise ValueError(f'Expected either arguments {required}')
        if country_name:
            country_name = country_name.lower()
            result = self.data[(self.data['CLDR display name'] == country_name) |
                               (self.data['UNTERM English Short'] == country_name) |
                               (self.data['UNTERM English Formal'] == country_name) |
                               (self.data['official_name_en'] == country_name)]
            options = (country_name, 'Country Name')
        elif alpha2:
            alpha2 = alpha2.upper()
            result = self.data[(self.data['ISO3166-1-Alpha-2'] == alpha2)]
            options = (alpha2, 'ISO3166-1-Alpha-2')
        elif alpha3:
            alpha3 = alpha3.upper()
            result = self.data[(self.data['ISO3166-1-Alpha-3'] == alpha3)]
            options = (alpha3, 'ISO3166-1-Alpha-3')
        elif geoname_id:
            geoname_id = str(float(geoname_id))
            result = self.data[(self.data['Geoname ID'] == geoname_id)]
            options = (geoname_id, 'geoname_id')
        export_data = self.send_result(result, *options)
        cleaned_export = self._clean_export(export_data)
        columns_to_rename = self.rename_cols
        cleaned_export = cleaned_export.rename(columns=columns_to_rename)
        dict_df = cleaned_export.to_dict(orient="list")
        dict_df = {x: dict_df[x][0] for x in dict_df}
        return SimpleJsonspace(**dict_df)

    def get_currency_table(*self, **kwargs):
        self = self[0]
        required = ["name", "short_code", "numeric_code"]
        full_name = kwargs.get("name")
        short_code = kwargs.get("short_code")
        numeric_code = kwargs.get("numeric_code")
        if all(x is None for x in {full_name, short_code, numeric_code}):
            raise ValueError(f'Expected either arguments {required}')
        if full_name:
            full_name = full_name.lower()
            result = self.data[(self.data['ISO4217-currency_name'] == full_name)]
            options = (full_name, 'currency')
        elif short_code:
            short_code = short_code.upper()
            result = self.data[(self.data['ISO4217-currency_alphabetic_code'] == short_code)]
            options = (short_code, 'currency code')
        elif numeric_code:
            numeric_code = str(numeric_code)
            result = self.data[(self.data['ISO4217-currency_numeric_code'] == numeric_code)]
            options = (numeric_code, 'currency number')
        export_data = self.send_result(result, *options)
        cleaned_export = self._clean_export(export_data)
        columns_to_rename = self.rename_cols
        cleaned_export = cleaned_export.rename(columns=columns_to_rename)
        return cleaned_export

    def get_continent_table(self, continent):
        continent_name = self.continents.get(continent.lower())
        if continent_name:
            result = self.data[(self.data['Continent'] == continent_name)]
            export_data = self.send_result(result, continent, 'continent')
            cleaned_export = self._clean_export(export_data)
            columns_to_rename = self.rename_cols
            cleaned_export = cleaned_export.rename(columns=columns_to_rename)
            return cleaned_export
        else:
            raise ValueError(f'I couldnt find any countries in continent {continent}')

    def _clean_export(self, data):
        ret_data = data.copy()
        upper_cols = [
            'CLDR display name',
            'UNTERM English Formal',
            'official_name_en',
            'ISO4217-currency_name'
        ]
        reversed_continents = {self.continents[i]: i.capitalize() for i in self.continents}
        for i in upper_cols:
            ret_data[i] = ret_data[i].apply(lambda x: x.capitalize())
        ret_data['Continent'] = ret_data["Continent"].apply(lambda x: reversed_continents.get(x))
        return ret_data

    def send_result(self, result, search_word, search_columns):
        if len(result):
            return result[self.active_columns]
        else:
            print(f'I couldnt find any countries with {search_columns} {search_word}')
