import logging
from worker.call_job import call_job

logger = logging.getLogger(__name__)


def files(*args, **kwargs):
    jobs = []
    for i in range(1000):
        jobs.append(call_job(_file, i))
    return jobs


def _file(filename):
    print("Here process file", filename)
