from flask import (
    Blueprint, render_template, request
)
from pathlib import Path
from svvs_report import build_report, find_driver

bp = Blueprint('web_report_app', __name__)

ROOT = Path(__file__).resolve().parent
FILES = ROOT / 'files'


@bp.route('/report/')
def report():
    files = request.args.get('files', FILES)
    order = request.args.get('order')
    result = build_report(files, order)
    return render_template('report.html', result=result)


@bp.route('/driver/')
def driver():
    files = request.args.get('files', FILES)
    order = request.args.get('order')
    driver_id = request.args.get('driver_id')
    result = build_report(files, order)
    if not driver_id:
        return render_template('drivers.html', driver_data=result)
    driver_data = find_driver(result, driver_id)
    return render_template('driver.html', driver_data=driver_data)
