import os
from projects import create_app
from projects import configs


enviroment = configs.config['development']

if os.getenv('PRODUCTION', default=False):
    enviroment = configs.config['production']

app = create_app(enviroment)