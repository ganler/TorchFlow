from .utility import setup_pip_env
import subprocess, os
from .io import record_exec_cmd_key, record_env_id_key

class env:
    env_name = None
    env_ver = None
    env_where = None
    model_name = None

    env_id = None # From DB.
    env_time = None # From DB.

    def __init__(self, env_name, env_ver, env_where, model_name):
        self.env_name = env_name
        self.env_ver = env_ver
        self.env_where = env_where
        self.model_name = model_name

    def run(self, rec_cmd):
        self.check_minimum()
        setup_pip_env(self.env_where)

        cmd = f'cd {self.env_where}; {rec_cmd}'
        sub_env = os.environ.copy()
        sub_env[record_env_id_key()] = str(self.env_id)
        sub_env[record_exec_cmd_key()] = rec_cmd
        subprocess.Popen(cmd, env=sub_env, shell=True)

    def check_minimum(self):
        if self.env_name == None or self.env_ver == None or self.env_where == None or self.model_name == None:
            raise Exception("Attribute With None Value!")