# encoding: utf-8
import os
import logging
from datetime import datetime, date

from rq import Queue

from worker.connection import conn

logger = logging.getLogger(__name__)


queue_name = os.getenv('QUEUE_NAME', 'default')
q = Queue(queue_name, connection=conn)


def call_job(func, *args, **kwargs):
    job = q.enqueue_call(func=func, args=args, **kwargs)
    parse_args = []
    for k in args:
        if k.__class__ in (datetime, date):
            parse_args.append(str(k))
        else:
            parse_args.append(k)
    job_id = job.get_id()
    response = {
        "message": "Job added in queue",
        "job_id": job.get_id(),
        "func_name": func.__name__,
        "args": parse_args,
        "kwargs": kwargs,
    }

    logger.info(f"Job added in queue. job_id => '{job_id}'", response=response)

    return response
