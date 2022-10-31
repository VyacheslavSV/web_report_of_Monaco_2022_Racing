# from pathlib import Path
# from flask import Flask, render_template, request, app
# from svvs_report import build_report, find_driver
#
# FILES = Path('../files')
# def app_flask_web():
#
#
#
#     @app.route('/hello11')
#     def hello():
#         return 'Hello, World11!'
#
#
#     @app.route('/report/', methods=['GET'])
#     def report():
#         order = request.args.get('order')
#         files = request.args.get('files', FILES)
#         result = build_report(files, order)
#         if order == 'desc':
#             return render_template('report.html', result=build_report(FILES, 'desc'))
#         elif files == isinstance(files, str):
#             return render_template('report.html', result=build_report(str))
#         else:
#             return render_template('report.html', result=result)
#
#
#     @app.route('/driver/', methods=['GET'])
#     def driver():
#         order = request.args.get('order')
#         files = request.args.get('files', FILES)
#         result = build_report(files, order)
#         driver_id = request.args.get('driver_id')
#
#         if driver_id:
#             driver_data = find_driver(result, driver_id)
#             return render_template('drivers.html', driver_data=driver_data)
#         elif order == 'desc':
#             return render_template('drivers.html', result=build_report(FILES, 'desc'))
#         else:
#             return render_template('drivers.html', result=result)
#     return app
#
# if __name__ == '__main__':
#     app_flask_web()
