'''
By Jiawei Liu.
'''

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# Init database.
os.system('sh ' + dir_path + '/create_torchflow.sh')

# Set data file dir.
from pathlib import Path
if 'TorchFlowPath' not in os.environ:
    os.environ['TorchFlowPath'] = str(Path.home()) + '/.TorchFlow'