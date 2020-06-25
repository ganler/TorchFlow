import os

def default_root_dir():
    return os.environ['TorchFlowPath']

def default_env_dir():
    directory = default_root_dir() + '/envs'
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def default_record_dir():
    directory = default_root_dir() + '/records'
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def save_snapshot(location):
    pass # TODO.