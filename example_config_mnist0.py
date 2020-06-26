from torchflow.register import register_environment
from torchflow.mysql import mysql_connector

import os

if __name__ == '__main__':
    register_environment(os.path.abspath('example_projects/mnist0'), 'mnist', 'v3')
    print(mysql_connector().glob_all_envs())