from flask_restful import Resource
# from flask import request, flash, render_template, redirect, url_for


class DataSet(Resource):
    def get(self):
        return 'DataSet get'

    def post(self):
        pass
