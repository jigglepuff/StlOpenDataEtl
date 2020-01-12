import os
import yaml


def get_yaml(yaml_file):
    '''
    Returns a YAML object
    '''
    with open(os.path.join(yaml_file), 'r') as yamlReader:
        return yaml.load(yamlReader, Loader=yaml.FullLoader)
