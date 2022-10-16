from flask import Flask, render_template, request
from svvs_report import build_report


def drivers_cod_name_dict(data):
    parsed_lines = []
    for line in data:
        abbr = str("".join(e[0] for e in str(line[0]).split())
                   + "".join(e[0] for e in str(line[1]).split()))[0:3]
        name = line[0]
        stat = ', '.join(line)
        dict_all = {'driver_id': abbr, 'name': name, abbr: stat}
        parsed_lines.append(dict_all)
    return parsed_lines


def fine(k):
    for dik in dict_all_info:
        if dik['driver_id'] == k:
            return dik.get(k)


app = Flask(__name__)

result = build_report('files')
dict_all_info = drivers_cod_name_dict(result)
dict_all_info_reverse = sorted(dict_all_info, key=lambda d: d['driver_id'], reverse=True)


@app.route('/report')
def index():
    return render_template('report.html', title='Common statistic', diction=result)


@app.route('/report/drivers/', methods=['GET'])
def drivers():
    driver_id = request.args.get('driver_id')
    order = request.args.get('order')

    if None is not driver_id:
        return str(fine(driver_id))
    elif None is not order:
        if order == 'desc':
            return render_template('drivers.html', title='List of drivers name and code',
                                   diction=dict_all_info_reverse)
    elif None is driver_id:
        return render_template('drivers.html', title='List of drivers name and code',
                               diction=dict_all_info)


@app.route('/page/', methods=['GET', 'POST'])
def page():
    driver_id = request.args.get('driver_id')
    if None is not driver_id:
        return str(fine(driver_id))


if __name__ == '__main__':
    app.run(debug=True)
