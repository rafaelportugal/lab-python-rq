# encoding: utf-8
import flask_restful as restful
from flask import Blueprint

from project.jobs.job_status import JobStatus


jobs_bp = Blueprint(
    'jobs', __name__,
)

api = restful.Api(jobs_bp)

api.add_resource(JobStatus, '/jobs/<job_key>')
