# encoding: utf-8
import os
from time import sleep

import flask_restful as restful

from worker.call_job import call_job
from helper import convert_dict_to_pascalcase
from project.batch.process import files


class FilesView(restful.Resource):
    def post(self):
        job_id = call_job(files)
        response = {
            'message': 'Job add on queue',
            'job_id': job_id
        }

        return convert_dict_to_pascalcase(response), 202
