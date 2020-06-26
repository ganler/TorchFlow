class record:
    model_name = None
    record_cmd = None
    record_loss_func = None
    record_loss = None
    model_size = None

    record_where = None
    env_id = None

    record_time = None
    record_id = None

    def __init__(self, model_name, record_cmd, record_loss_func, record_loss, model_size, record_where, env_id):
        self.record_loss_func = record_loss_func
        self.model_name = model_name
        self.record_cmd = record_cmd
        self.record_loss = record_loss
        self.model_size = model_size
        self.env_id = env_id
        self.record_where = record_where

    def check_minimum(self):
        if self.model_name == None or \
                self.record_cmd == None or \
                self.record_loss_func == None or \
                self.record_loss == None or \
                self.model_size == None or \
                self.env_id == None or \
                self.record_where == None:
            raise Exception("Attribute With None Value!")

    def __repr__(self):
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
        ret = ''
        ret += f'model_name = {self.model_name}\n'
        ret += f'record_cmd = {self.record_cmd}\n'
        ret += f'record_loss_func = {self.record_loss_func}\n'
        ret += f'record_loss = {self.record_loss}\n'
        ret += f'model_size = {self.model_size}\n'
        ret += f'record_where = {self.record_where}\n'
        ret += f'env_id = {self.env_id}\n'

        ret += f'record_time = {self.record_time}\n'
        ret += f'record_id = {self.record_id}\n'
        return ret