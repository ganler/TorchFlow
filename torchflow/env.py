from .utility import setup_pip_env
import subprocess, os
from .io import record_exec_cmd_key, record_env_id_key

class env:
    env_name = None
    env_ver = None
    env_where = None

    env_id = None # From DB.
    env_time = None # From DB.

    def __init__(self, env_name, env_ver, env_where):
        self.env_name = env_name
        self.env_ver = env_ver
        self.env_where = env_where

    def run(self, rec_cmd):
        self.check_minimum()
        setup_pip_env(self.env_where)

        cmd = f'cd {self.env_where}; {rec_cmd}'
        sub_env = os.environ.copy()
        sub_env[record_env_id_key()] = str(self.env_id)
        sub_env[record_exec_cmd_key()] = rec_cmd
        process = subprocess.Popen(cmd, env=sub_env, shell=True)
        process.wait()
        if process.poll() == 0:
            print(process.communicate()[1])
        else:
            print("失败")

    def check_minimum(self):
        if self.env_name == None or self.env_ver == None or self.env_where == None:
            raise Exception("Attribute With None Value!")

    def __repr__(self):
        '''
    env_name = None
    env_ver = None
    env_where = None

    env_id = None # From DB.
    env_time = None # From DB.
        '''
        ret = ''
        ret += f'env_name = {self.env_name}\n'
        ret += f'env_ver = {self.env_ver}\n'
        ret += f'env_where = {self.env_where}\n'
        ret += f'env_id = {self.env_id}\n'
        ret += f'env_time = {self.env_time}\n'
        return ret