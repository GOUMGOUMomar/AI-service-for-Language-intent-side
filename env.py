import json
import os


class ConfigLoader:

    def __init__(self, config_file_path):
        self.config_file_path = config_file_path

    def load_config(self):
        try:
            with open(self.config_file_path) as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading configuration from {self.config_file_path}: {e}")
            return None

    def set_environment_variables(self):

        config_data = self.load_config()
        if config_data:
            for key, value in config_data.items():
                os.environ[key] = value



