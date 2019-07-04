# encoding: utf-8
from flask import Flask

from project.healthcheck import healthcheck_bp
from project.jobs import jobs_bp
from project.batch import files_bp


app = Flask(__name__)
app.register_blueprint(healthcheck_bp)
app.register_blueprint(jobs_bp, url_prefix='/v1')
app.register_blueprint(files_bp, url_prefix='/v1')
