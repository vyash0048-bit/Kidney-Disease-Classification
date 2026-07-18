import os
from cnnClassifier import logger
import gdown
from cnnClassifier.entity.config_entity import TrainingConfig

class Training:

    def __init__(self, config: TrainingConfig):
        self.config = config


    def download_file(self):
        '''
        Download file from Google Drive using gdown library.
        '''

        try:
            trained_url = self.config.trained_URL
            trained_model_path = self.config.trained_model_path
            os.makedirs("artifacts/training", exist_ok=True)
            logger.info(f"Downloading file from {trained_url} to {trained_model_path}")

            file_id = trained_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix + file_id, str(trained_model_path), quiet=False)

            logger.info(f"File downloaded from {trained_url} to {trained_model_path}")
        except Exception as e:
            raise e
    
    