import configparser

CONFIG_PATH = "../config/config.cfg"

def read_config():
    """
    Reads the configuration file has a fallback to the dev_config.cfg file
    :return: <dict> The configuration
    """

    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return config