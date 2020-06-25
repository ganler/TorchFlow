from . import record

class env:
    env_name = None
    env_ver = None
    env_where = None
    model_name = None

    env_id = None # From DB.
    env_time = None # From DB.

    def __init__(self, env_name, env_ver, env_where, model_name):
        self.env_name = env_name
        self.env_ver = env_ver
        self.env_where = env_where
        self.model_name = model_name

    def run(self) -> record:
        pass # Return Record.

    def _check_before_run(self):
        if self.env_name == None or self.env_ver == None or self.env_where == None or self.model_name == None:
            raise Exception("Attribute With None Value!")

    def _to_mysql(self):
        pass # To MySQL.

    def _from_mysql(self):
        pass # From MySQL