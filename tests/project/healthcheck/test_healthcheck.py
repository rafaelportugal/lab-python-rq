# encoding: utf-8
import json
from unittest import TestCase, main
from unittest.mock import patch

from project import app


def mock_call_job():
    return {
        "message": "Job added in queue",
        "job_id": 'b2054055-5e5a-4e3d-9acc-3d712499b5e4',
        "func_name": "test",
        "args": [],
        "kwargs": {},
    }


class TestHealthcheck(TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('worker.call_job.call_job')
    def test_healthcheck_mock_call_job(self, mock):
        expected_response = {
            "message": "Job added in queue",
            "jobId": 'b2054055-5e5a-4e3d-9acc-3d712499b5e4',
            "funcName": "test",
            "args": [],
            "kwargs": {},
        }

        mock.return_value = mock_call_job

        response = self.app.get('/healthcheck')
        self.assertEqual(json.loads(response.get_data()), expected_response)

    def test_return_correct_status_code_healthcheck(self):
        response = self.app.get('/healthcheck')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    main()
