from flask import Flask, render_template
from report import *

app = Flask(__name__)

result = build_report('files')
drivers = drivers_cod_name(build_report('files'))


@app.route('/report')
def index():
    return render_template('report.html', title='Common statistic', result=result)


@app.route('/report/drivers')
def drivers():
    return render_template('drivers.html', title='List of drivers name and code', drivers=drivers)

#
# @app.route('/report/drivers/?driver_id=SVF')
# def index():
#     return render_template('info_about_a_driver.html')
#
#
# @app.route('/drivers/?order=desc')
# def index():
#     return render_template('order_desc.html')


if __name__ == '__main__':
    app.run(debug=True)
