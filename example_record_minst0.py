from torchflow.mysql import mysql_connector

if __name__ == '__main__':
    connctor = mysql_connector()
    envs = connctor.glob_all_envs()
    for env in envs:
        if env.env_name == 'minst' and env.env_ver == 'basic':
            print(f'Running: {env}')
            env.run('python main.py --epochs=1')