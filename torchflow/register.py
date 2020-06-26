from .mysql import mysql_connector
from .io import save_snapshot
from .env import env

def register_environment(location, env_name, env_ver):
    aim_where = save_snapshot(location, env_name, env_ver)
    mysql_connector().upload_env(env(env_name, env_ver, aim_where))