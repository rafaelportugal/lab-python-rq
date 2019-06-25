# encoding: utf-8
import os
from time import sleep

import flask_restful as restful

from worker.call_job import call_job
from helper import convert_dict_to_pascalcase


def test(num):
    sleep(num)
    return {
        "message": "Job health-check executado com sucesso",
        "success": True
    }


class HealthCheck(restful.Resource):
    def get(self):
        health_timeout = os.getenv("HEALTH_CHECK_TIMEOUT", 2)
        response = call_job(test, health_timeout, timeout=300, result_ttl=300)

        return convert_dict_to_pascalcase(response), 200
