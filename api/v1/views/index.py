#!/usr/bin/python3
"""
routing app views
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """status OK"""
    return jsonify({"status": "OK"})