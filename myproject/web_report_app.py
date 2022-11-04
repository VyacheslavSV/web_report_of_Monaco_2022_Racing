from flask import (
    Blueprint, render_template, request
)
from pathlib import Path
from svvs_report import build_report, find_driver
from werkzeug.exceptions import abort

bp = Blueprint('hello', __name__)

ROOT = Path(__file__).resolve().parent
FILES = ROOT / 'files'


@bp.route('/report/')
def report():
    order = request.args.get('order')
    files = request.args.get('files', FILES)
    result = build_report(files, order)
    return render_template('report.html', result=result)


@bp.route('/driver/')
def driver():
    order = request.args.get('order')
    files = request.args.get('files', FILES)
    driver_id = request.args.get('driver_id')
    result = build_report(files, order)
    if driver_id:
        driver_data = find_driver(result, driver_id)
        render_template('driver.html', driver_data=driver_data)
    return render_template('drivers.html', driver_data=result)



