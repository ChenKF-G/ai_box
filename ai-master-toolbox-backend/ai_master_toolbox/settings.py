import os

from .settings_common import *

# 根据 DEBUG 环境变量决定加载哪个设置文件
env_debug = os.environ.get('DEBUG')
if env_debug == 'False':
    DEBUG = False
    from .settings_production import *
else:
    DEBUG = True
    from .settings_debug import *

