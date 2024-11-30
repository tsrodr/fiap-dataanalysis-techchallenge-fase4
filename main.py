from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
import os
from utils.spark_postgres import SparkPostgres
from utils.ipea_data import IpeaData
import joblib
import pandas as pd
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA


class Processar:
    def __init__(self, spark, host, port, database, user,
                 password, schema, org_table, ipea_url, sercodigo):
        self.spark = spark
        self.spark_postgres = SparkPostgres(spark, host, port,
                                            database, user, password)
        self.schema = schema
        self.org_table = org_table
        self.sercodigo = sercodigo
        self.ipeadata = IpeaData(ipea_url)

    def run(self):
        df = self.ipeadata_run()
        df = self.preprocess_data(df)
        df_preparado = self.prepare_data(df)
        treino = self.get_training_data(df_preparado)
        modelo_arima = self.train_model(treino)
        self.save_model(modelo_arima, 'modelo/auto_arima.joblib')
        modelo_carregado = self.load_model('modelo/auto_arima.joblib')
        forecast = self.make_forecast(modelo_carregado, h=30)
        self.save_forecast(forecast, './output/sor/forecast2.csv')

    def ipeadata_run(self):
        table_ipea = next(item for item in self.org_table if item['name'] == "IpeaData")
        df = self.ipeadata.carregar(self.sercodigo, table_ipea['file'])
        if df is not None:
            df_spark = self.spark.createDataFrame(df)
            df_spark = df_spark.withColumn("valdata", to_date(col("valdata")))
            df_spark = df_spark.withColumn("valvalor", col("valvalor").cast("float"))
            self.spark_postgres.save_to_postgres(df_spark, self.schema, table_ipea['table'])
            return df
        return None

    def preprocess_data(self, df):
        df = df.drop(columns=["sercodigo", "tercodigo", "nivnome", "dt_pst"])
        df = df.rename(columns={"valdata": "data", "valvalor": "preco"})
        df = df.dropna(subset=["preco", "data"])
        df = df.sort_values(by="data", ascending=False)
        df['data'] = pd.to_datetime(df['data'], utc=True).dt.tz_localize(None).dt.normalize()
        return df

    def prepare_data(self, df):
        df_preparado = df[['data', 'preco']].rename(columns={'data': 'ds', 'preco': 'y'})
        df_preparado['unique_id'] = 'Preco'
        df_preparado.dropna(inplace=True)
        return df_preparado

    def get_training_data(self, df_preparado):
        return df_preparado.loc[df_preparado['ds'] >= '2000-01-01']

    def train_model(self, treino):
        modelo_arima = StatsForecast(models=[AutoARIMA(season_length=5)], freq='B', n_jobs=-1)
        modelo_arima.fit(treino)
        return modelo_arima

    def save_model(self, model, filepath):
        joblib.dump(model, filepath)

    def load_model(self, filepath):
        return joblib.load(filepath)

    def make_forecast(self, model, h):
        forecast = model.predict(h=h, level=[90])
        forecast = (
            forecast[['ds', 'AutoARIMA']]
            .reset_index(drop=True)
            .rename(columns={'ds': 'data', 'AutoARIMA': 'preco_previsto_brent'})
        )
        forecast['preco_previsto_brent'] = forecast['preco_previsto_brent'].apply(lambda x: round(x, 2))
        return forecast

    def save_forecast(self, df, filepath):
        table_forecast = next(item for item in self.org_table if item['name'] == "Forecast")
        df_spark = self.spark.createDataFrame(df)
        self.spark_postgres.save_to_postgres(df_spark, self.schema, table_forecast['table'])


def main():
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_DATABASE")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    schema = os.getenv("DB_SCHEMA")
    org_table = [ { "name": "IpeaData", "table": "tb_eia366_pbrent366", "file": "./output/sor/ipeadata.csv" },
                { "name": "Forecast", "table": "tb_eia366_pbrent366_forecast", "file": "./output/sor/forecast.csv" } ]

    ipea_url = "http://www.ipeadata.gov.br/api/odata4/"
    sercodigo = "EIA366_PBRENT366"

    spark = SparkSession.builder.appName("Processar").getOrCreate()
    processar = Processar(spark, host, port, database, user,
                          password, schema, org_table, ipea_url, sercodigo)
    processar.run()


if __name__ == "__main__":
    main()
