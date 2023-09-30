## data_processor.py

import pandas as pd
from typing import Union
import logging

class DataProcessor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def load_data(self, file_path: str) -> Union[pd.DataFrame, None]:
        """
        Load data from a CSV file.
        
        Args:
            file_path (str): The path to the CSV file.
        
        Returns:
            DataFrame: A pandas DataFrame containing the loaded data.
        """
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as e:
            self.logger.error(f"Error occurred while loading data: {e}")
            return None

    def process_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, None]:
        """
        Process the loaded data.
        
        Args:
            data (DataFrame): The loaded data.
        
        Returns:
            DataFrame: A pandas DataFrame containing the processed data.
        """
        try:
            # Assuming some processing is needed, like filling missing values, normalizing, etc.
            processed_data = data.fillna(0)
            return processed_data
        except Exception as e:
            self.logger.error(f"Error occurred while processing data: {e}")
            return None
