# This lib handles loading config from config.json. If config.json is not
# found, it will create one with default values.
#
################################################################################
import json
import os


# Class for config loading
class Config:
    def __get_hooks_path(self):
        """Get hooks path from Git global config"""
        return os.popen("git config --global core.hooksPath").read().strip()

    def __get_config_path(self):
        """Get config path using relative path from hooks path"""
        return os.path.join(self.__get_hooks_path(), "../config/config.json")

    def __config_exists(self):
        """Check if config exists"""
        return os.path.exists(self.__get_config_path())

    def __create_config(self):
        """Create config with default values. Copy config.json.example to config.json"""
        # Get config path
        config_path = self.__get_config_path()

        # Get example config path
        example_config_path = os.path.join(
            self.__get_hooks_path(), "../config/config.json.example"
        )

        # Copy example config to config
        os.system("cp " + example_config_path + " " + config_path)

    def __init__(self):
        """Initialize config"""
        # Check if config exists
        if not self.__config_exists():
            print("Config not found. Creating config...", end="")
            # Create config
            try:
                self.__create_config()
                print("OK!")
            except Exception as e:
                print("FAILED!")
                raise Exception("Failed to create config.") from e

        # Load config
        self.__load_config()

    def __load_config(self):
        """Load config"""
        # Get config path
        config_path = self.__get_config_path()

        # Open config file (UTF-8)
        with open(config_path, "r", encoding="utf-8") as config_file:
            # Load config
            self.__config = json.load(config_file)

    def get_config(self):
        """Get config"""
        return self.__config
