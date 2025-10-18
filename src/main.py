from consts import ASSETS_DIR, FILE_NAME, SOURCE_URL
from .get_file import download_file
from .etl import ETL



download_file(SOURCE_URL, ASSETS_DIR / FILE_NAME)

etl = ETL(ASSETS_DIR / FILE_NAME)
etl.run_etl()