# encoding: utf-8
from flask_restful import Api
from flask import Blueprint

from project.batch.view import FilesView

files_bp = Blueprint(
    'files', __name__,
)

api = Api(files_bp)

api.add_resource(FilesView, '/files')
