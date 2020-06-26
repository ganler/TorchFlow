from torchflow.mysql import mysql_connector

if __name__ == '__main__':
    connctor = mysql_connector()
    print(connctor.glob_all_envs())
    print(connctor.glob_all_records())