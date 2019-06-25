# encoding: utf-8
from flask_restful import Api
from flask import Blueprint

from project.healthcheck.healthcheck import HealthCheck

healthcheck_bp = Blueprint(
    'healthcheck', __name__,
)

api = Api(healthcheck_bp)

api.add_resource(HealthCheck, '/healthcheck')
