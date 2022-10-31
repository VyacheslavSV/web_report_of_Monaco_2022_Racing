import pytest
from flask import Flask
from web_report import create_app


def test_report(client):
    app = Flask(__name__)
    response = client.get('/report1/')
    assert response.data == 200

#app = flask.Flask(__name__)

# with app.test_request_context('/?name=Peter'):
#     assert flask.request.path == '/'
#     assert flask.request.args['name'] == 'Peter'
#


if __name__ == '__main__':
    pytest.main()
