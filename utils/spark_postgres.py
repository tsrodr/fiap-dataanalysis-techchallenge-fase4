from pyspark.sql import SparkSession
from pyspark.sql.functions import current_date


class SparkPostgres:
    """
    A utility class for interacting with PostgreSQL using Apache Spark.
    Attributes:
        spark (SparkSession): The Spark session object.
        url (str): The JDBC URL for connecting to the PostgreSQL database.
        properties (dict): The connection properties including user, password, and driver.
    Methods:
        __init__(spark, host, port, database, user, password):
            Initializes the SparkPostgres instance with the given parameters.
        load_csv(file_path):
            Loads a CSV file into a Spark DataFrame.
            Args:
                file_path (str): The path to the CSV file.
            Returns:
                DataFrame: The loaded Spark DataFrame if the file exists, otherwise None.
        save_to_postgres(df, schema, table):
            Saves a Spark DataFrame to a PostgreSQL table.
            Args:
                df (DataFrame): The Spark DataFrame to save.
                schema (str): The schema name in PostgreSQL.
                table (str): The table name in PostgreSQL.
    """
    def __init__(self, spark: SparkSession, host: str,
                 port: str, database: str, user: str,
                 password: str):
        self.spark = spark
        self.url = f"jdbc:postgresql://{host}:{port}/{database}"
        self.properties = {
            "user": user,
            "password": password,
            "driver": "org.postgresql.Driver"
        }

    def save_to_postgres(self, df, schema, table):
        # Adicionar a coluna 'data processamento' com a data atual
        df = df.withColumn('dt_pst', current_date())
        df.write.jdbc(
            url=self.url,
            table=f"{schema}.{table}",
            mode="overwrite",
            properties=self.properties
            )
