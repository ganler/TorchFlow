from torchflow.register import register_environment
from torchflow.mysql import mysql_connector

import os

if __name__ == '__main__':
    register_environment(os.path.abspath('example_projects/minst1'), 'minst', 'bignet')
    print(mysql_connector().glob_all_envs())