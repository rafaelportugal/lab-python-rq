# encoding: utf-8
import os
import json
import signal
from unittest import TestCase, main

from project import app


def mock_call_job():
    return {
        "message": "Job added in queue",
        "job_id": 'b2054055-5e5a-4e3d-9acc-3d712499b5e4',
        "func_name": "test",
        "args": [],
        "kwargs": {},
    }


class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        raise Exception(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)


class TestJobStatus(TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.headers = {"APP_TOKEN": os.getenv("SECRET_KEY")}
        self.url = "v1/jobs/{job_id}"

    def tearDown(self):
        pass

    def test_jobs_not_found(self):
        response = self.app.get(self.url.format(job_id="12324"),
                                headers=self.headers)
        self.assertEqual(response.status_code, 404)

    def test_jobs_in_queue(self):
        response = self.app.get('/healthcheck')

        job_id = json.loads(response.get_data()).get("jobId")
        response = self.app.get(self.url.format(job_id=job_id),
                                headers=self.headers)

        self.assertEqual(response.status_code, 202)

    def test_job_completed(self):
        response = self.app.get('/healthcheck')
        job_id = json.loads(response.get_data()).get("jobId")
        self.assertEqual(response.status_code, 200)
        healthcheck_timeout = os.getenv("HEALTH_CHECK_TIMEOUT", 2) + 3
        has_completed = False
        with timeout(seconds=healthcheck_timeout):
            while not has_completed:
                resp = self.app.get(self.url.format(job_id=job_id),
                                    headers=self.headers)
                if resp.status_code == 200:
                    has_completed = True
                    break
        self.assertTrue(has_completed)


if __name__ == "__main__":
    main()
