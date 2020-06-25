class record:
    model_name = None
    record_cmd = None
    record_loss_func = None

    record_loss = None
    model_size = None

    record_time = None
    record_id = None
    env_id = None

    def __init__(self, model_name, record_cmd, record_loss_func, record_loss, model_size):
        self.record_loss_func = record_loss_func
        self.model_name = model_name
        self.record_cmd = record_cmd
        self.record_loss = record_loss
        self.model_size = model_size

    def _check_before_run(self):
        if self.model_name == None or self.record_cmd == None or self.record_loss_func == None or self.record_loss == None or self.model_size == None:
            raise Exception("Attribute With None Value!")

    def _to_mysql(self):
        self._check_before_run()
        pass  # To MySQL.