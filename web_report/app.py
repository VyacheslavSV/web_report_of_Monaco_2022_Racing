from pathlib import Path
from flask import Flask, render_template, request
from svvs_report import build_report, find_driver


app = Flask(__name__)
FILES = Path('../files')


@app.route('/report1/', methods=['GET'])
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


if __name__ == '__main__':
    app.run(debug=True)
