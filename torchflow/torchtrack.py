import torch
import os
from .record import record
from .mysql import mysql_connector
from .io import record_env_id, record_exec_cmd, default_record_dir

class track:
    model_ref: torch.nn.Module = None
    loss_fn_ref: torch.optim = None
    loss_val = None

    def __init__(self, model: torch.nn.Module):
        self.model_ref = model

    def track_loss_fn(self, opt: torch.optim):
        self.loss_fn_ref = opt

    def track_loss_val(self, val):
        self.loss_val = val

    def generate_record(self):
        connctor = mysql_connector()
        # model_name, record_cmd, record_loss_func, record_loss, model_size)
        model_save_path = default_record_dir() + '/' + record_env_id() + '-' + self.model_ref.__class__.__name__ + '.pth'
        torch.save(self.model_ref, model_save_path)
        # model_name, record_cmd, record_loss_func, record_loss, model_size, record_where, env_id
        rec = record(
            self.model_ref.__class__.__name__,
            record_exec_cmd(),
            self.loss_fn_ref.__class__.__name__,
            self.loss_val,
            sum([param.nelement() for param in self.model_ref.parameters()]),
            model_save_path,
            int(record_env_id())
        )
        connctor.upload_record(rec)