from torchflow.mysql import mysql_connector
from torchflow.viz import viz_model_size

if __name__ == '__main__':
    connctor = mysql_connector()
    print(connctor.glob_all_envs())
    print(connctor.glob_all_records())
    viz_model_size()