import os
from  projects.configs import config
from  projects import create_app


enviroment = config['development']

if os.getenv('PRODUCTION', default=False):
    enviroment = config['production']

app = create_app(enviroment)