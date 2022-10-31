import os
from pathlib import Path
from flask import Flask, render_template, request
from svvs_report import build_report, find_driver
from flask import Flask

FILES = Path('../files')


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello11')
    def hello1():
        return 'Hello, World11!'

    @app.route('/report/', methods=['GET'])
    def report():
        order = request.args.get('order')
        files = request.args.get('files', FILES)
        result = build_report(files, order)
        if order == 'desc':
            return render_template('report.html', result=build_report(FILES, 'desc'))
        elif files == isinstance(files, str):
            return render_template('report.html', result=build_report(str))
        else:
            return render_template('report.html', result=result)

    @app.route('/driver/', methods=['GET'])
    def driver():
        order = request.args.get('order')
        files = request.args.get('files', FILES)
        result = build_report(files, order)
        driver_id = request.args.get('driver_id')

        if driver_id:
            driver_data = find_driver(result, driver_id)
            return render_template('drivers.html', driver_data=driver_data)
        elif order == 'desc':
            return render_template('drivers.html', result=build_report(FILES, 'desc'))
        else:
            return render_template('drivers.html', result=result)

    return app
