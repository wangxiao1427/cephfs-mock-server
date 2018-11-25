from app.resources import api
from .dataset import DataSet
from .datasource import DataSource

api.add_resource(DataSet, '/dataset')
api.add_resource(DataSource, '/datasource')
