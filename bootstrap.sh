#!/bin/bash
export FLASK_APP=./cashman/index.py
source ~/python_environments/flask/bin/activate
flask run -h 0.0.0.0
