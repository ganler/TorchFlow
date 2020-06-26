from torchflow.register import register_environment
from torchflow.mysql import mysql_connector

import os

if __name__ == '__main__':
    register_environment(os.path.abspath('example_projects/minst0'), 'minst', 'basic')
    print(mysql_connector().glob_all_envs())