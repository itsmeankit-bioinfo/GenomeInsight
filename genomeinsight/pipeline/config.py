import yaml


def load_config(file):

    with open(file) as f:

        return yaml.safe_load(f)