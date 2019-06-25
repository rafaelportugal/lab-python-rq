#!/usr/bin/env python
import os

from rq import Worker, Queue, Connection
from worker.connection import conn

queue_name = os.getenv('QUEUE_NAME', 'default')
listen = [queue_name]


def main():
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
