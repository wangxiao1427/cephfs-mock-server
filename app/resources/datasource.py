from flask_restful import Resource
# from flask import request, flash, render_template, redirect, url_for


class DataSource(Resource):
    def get(self):
        return 'DataSource get'

    def post(self):
        pass
