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
        try:
            # Get hooks path from Git global config
            return os.popen("git config --global core.hooksPath").read().strip()
        except Exception as e:
            raise RuntimeError(
                "Failed to get hooks path from Git. Is it installed?"
            ) from e

    def __get_config_path(self):
        """Get config path using relative path from hooks path"""
        return os.path.join(self.__get_hooks_path(), self.relative_config_path)

    def __config_exists(self):
        """Check if config exists"""
        return os.path.exists(self.__get_config_path())

    def __create_config(self):
        """Create config with default values. Copy config.json.example to config.json"""
        # Get config path
        config_path = self.__get_config_path()

        # Get example config path
        example_config_path = os.path.join(
            self.__get_hooks_path(), self.relative_config_path_example
        )

        # Copy example config to config
        os.system("cp " + example_config_path + " " + config_path)

    def __init__(
        self,
        relative_config_path="../config/config.json",
        relative_example_config_path="../config/config.json.example",
    ):
        """Initialize config"""
        self.relative_config_path = relative_config_path
        self.relative_config_path_example = relative_example_config_path
        # Check if config exists
        if not self.__config_exists():
            print("Config not found. Creating config...", end="")
            # Create config
            try:
                self.__create_config()
                print("OK!")
            except Exception as e:
                print("FAILED!")
                raise OSError("Failed to create config.") from e

        # Load config
        self.__load_config()

    def __load_config(self):
        """Load config"""
        # Get config path
        config_path = self.__get_config_path()

        try:
            # Open config file (UTF-8)
            with open(config_path, "r", encoding="utf-8") as config_file:
                # Load config
                self.__config = json.load(config_file)
        except Exception as e:
            raise OSError("Failed to load config.") from e

    def get_config(self):
        """Get config"""
        return self.__config
