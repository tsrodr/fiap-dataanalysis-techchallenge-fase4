import requests as req
import pandas as pd


class IpeaData:
    def __init__(self, url):
        self.url = url

    def _basic_api_call(self, consulta):
        try:
            response = req.get(consulta)
            response.raise_for_status()
            json_response = response.json()
            return pd.DataFrame(json_response.get('value', []))
        except (req.RequestException, ValueError, KeyError):
            return None

    def get_metadados(self, sercodigo=None):
        url_partial = f"{self.url}Metadados"
        if sercodigo:
            url_partial += f"('{sercodigo}')"
        return self._basic_api_call(url_partial)

    def get_valores(self, sercodigo):
        url_partial = f"{self.url}Metadados('{sercodigo}')/Valores"
        return self._basic_api_call(url_partial)

    def carregar(self, sercodigo, file_name):
        df = self.get_valores(sercodigo)
        if df is not None:
            df.columns = [col.lower() for col in df.columns]
            return df
