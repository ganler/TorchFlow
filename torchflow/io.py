import os
from distutils.dir_util import copy_tree

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

def save_snapshot(location, env_name, env_ver):
    aim_loc = default_env_dir() + f'/{env_name}-{env_ver}'
    copy_tree(location, aim_loc)

def record_exec_cmd_key():
    return 'TorchFlowCmd'

def record_env_id_key():
    return 'TorchFlowEnvID'

def record_exec_cmd():
    return os.environ[record_exec_cmd_key()]

def record_env_id():
    return os.environ[record_env_id_key()]