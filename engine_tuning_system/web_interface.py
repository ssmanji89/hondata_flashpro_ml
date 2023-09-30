## web_interface.py

from flask import Flask, jsonify
import pandas as pd
import logging
from typing import Dict, Any

class WebInterface:
    def __init__(self, app: Flask):
        self.app = app
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def display_data(self, data: pd.DataFrame) -> None:
        """
        Display the processed data.
        
        Args:
            data (DataFrame): The processed data.
        """
        @self.app.route('/display_data', methods=['GET'])
        def display_data_route():
            try:
                # Convert DataFrame to JSON
                data_json = data.to_json(orient='records')
                return jsonify(data_json)
            except Exception as e:
                self.logger.error(f"Error occurred while displaying data: {e}")
                return jsonify(error=str(e)), 500

    def display_recommendations(self, parameters: Dict[str, Any]) -> None:
        """
        Display the recommended tuning parameters.
        
        Args:
            parameters (dict): A dictionary containing the predicted parameters.
        """
        @self.app.route('/display_recommendations', methods=['GET'])
        def display_recommendations_route():
            try:
                return jsonify(parameters)
            except Exception as e:
                self.logger.error(f"Error occurred while displaying recommendations: {e}")
                return jsonify(error=str(e)), 500
