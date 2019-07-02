#!/usr/bin/env python
import os

from project import app
from worker.main import main
from multiprocessing import Process

env = os.environ.get('APP_SETTINGS', 'DevelopmentConfig')
app.config.from_object('config.{}'.format(env))


if __name__ == '__main__':

    process = Process(target=main)
    process.start()
    app.run(host='0.0.0.0',
            port=app.config.get('PORT'),
            processes=app.config.get('PROCESSES'), )
