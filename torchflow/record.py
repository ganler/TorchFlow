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