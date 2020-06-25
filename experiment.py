import mysql.connector
import torchflow
from pip_module_scanner.scanner import Scanner, ScannerException

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="torchflow",  # 数据库用户名
        passwd="TorchFlow@Jiawei233",  # 数据库密码
        database = "torchflow"
    )

    mycursor = mydb.cursor()

    env_name=  'fk'
    env_ver = 'uk'

    # try:
        # mycursor.execute(f"insert into env set env_id='{2}', model_name='{'model_namexxx'}', env_where='{'env_wherexxx'}';")
        # mydb.commit()
    mycursor.execute(f"select * from env;")
        # for res in mycursor.fetchall():
    for f in mycursor.fetchall():
        print(f[0])
        mycursor.execute(f'select * from env_meta where env_id={f[0]};')
        print(mycursor.fetchone())
    # except Exception as e:
    #     print(e)
    #     mydb.rollback()
    # try:
        # 执行sql语句
    # mydb.rollback()

    # except:
    #     # 发生错误时回滚
    #     mydb.rollback()

    # print(mycursor.execute(f"select env_id from env_meta where env_name='hello' and env_ver='0.1';"))