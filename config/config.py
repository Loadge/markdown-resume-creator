import yaml

def load_configuration(config_file_path: str='config.yaml'):
    """Load a yaml file 

    :param str config_file_path: path to the config file
        By default, the general config file is loaded
    :return dict: the config file in dict format
    """
    with open(config_file_path, 'r') as stream:
        data_loaded = yaml.safe_load(stream)

    