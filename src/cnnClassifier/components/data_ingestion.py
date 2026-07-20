import os
from pathlib import Path
import zipfile
import gdown
from cnnClassifier.utils.common import get_size
from cnnClassifier import logger
from cnnClassifier.entity.config_entity import (DataIngestionConfig)


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        '''
        Download file from Google Drive using gdown library.
        '''

        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)

            if os.path.exists(zip_download_dir):
                logger.info(f"File already exists at {zip_download_dir} of size: {get_size(Path(zip_download_dir))}. Skipping download.")
                return

            logger.info(f"Downloading file from {dataset_url} to {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix + file_id, zip_download_dir, quiet=False)

            logger.info(f"File downloaded from {dataset_url} to {zip_download_dir}")

        except Exception as e:
            raise e

    def extract_zip_file(self):
        """
        Extract the downloaded zip file to the specified directory.
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)