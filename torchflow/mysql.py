import mysql.connector
from .env import env
from .record import record

class mysql_connector:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",  # 数据库主机地址
            user="torchflow",  # 数据库用户名
            passwd="TorchFlow@Jiawei233",  # 数据库密码
            database="torchflow"
        )
        self.cursor = self.db.cursor()

# env_id | env_where | env_time
# env_id | env_name | env_ver
    def glob_all_envs(self):
        self.cursor.execute(f"select * from env;")
        ret = []
        for fetch in self.cursor.fetchall():
            self.cursor.execute(f"select env_name, env_ver from env_meta where env_id={fetch[0]};")
            meta_fetch = self.cursor.fetchone()
            environ = env(meta_fetch[0], meta_fetch[1], fetch[1])
            environ.env_id = fetch[0]
            environ.env_time = fetch[-1]
            ret.append(environ)
        return ret

    def glob_all_records(self):
        '''
    model_name = None
    record_cmd = None
    record_loss_func = None
    record_loss = None
    model_size = None

    record_where = None
    env_id = None

    record_time = None
    record_id = None
        '''

        ''' DB
| record_id            | int unsigned | NO   | PRI | NULL              | auto_increment    |
| model_name           | varchar(64)  | NO   |     | NULL              |                   |
| env_id               | int unsigned | NO   | MUL | NULL              |                   |
| record_cmd           | varchar(512) | YES  |     | NULL              |                   |
| record_loss_function | varchar(128) | NO   |     | NULL              |                   |
| record_loss          | double       | NO   |     | NULL              |                   |
| record_time          | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| record_where         | varchar(512) | NO   | UNI | NULL              |                   |
| model_size           | int unsigned | NO   |     | NULL              |

        '''
        self.cursor.execute(f"select * from record;")
        ret = []
        for fetch in self.cursor.fetchall():
            rec = record(fetch[1], fetch[3], fetch[4], fetch[5], fetch[-1], fetch[-2], fetch[2]);
            rec.record_time = fetch[-3]
            rec.record_id = fetch[0]
            ret.append(rec)
        return ret

    def upload_record(self, rec: record):
        rec.check_minimum()
        print(rec.env_id)
        self.cursor.execute(f"insert into record set model_name='{rec.model_name}', env_id={int(rec.env_id)}, record_cmd='{rec.record_cmd}', record_loss_function='{rec.record_loss_func}', record_loss={rec.record_loss}, record_where='{rec.record_where}', model_size={rec.model_size};")
        self.db.commit()

    def upload_env(self, environ: env):
        environ.check_minimum()
        self.cursor.execute(f"insert into env_meta set env_name='{environ.env_name}', env_ver='{environ.env_ver}';")
        self.db.commit()
        self.cursor.execute(f"select env_id from env_meta where env_name='{environ.env_name}' and env_ver='{environ.env_ver}';")
        env_id = self.cursor.fetchone()[0]
        self.cursor.execute(f"insert into env set env_id='{env_id}', env_where='{environ.env_where}';")
        self.db.commit()