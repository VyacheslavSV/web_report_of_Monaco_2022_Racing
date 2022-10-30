import pytest
from flask import Flask
import web_report.web_rep_app


def test_report(test_client, captured_templates):
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/report'

    response = client.get(url)
    assert response.get_data() == q
    assert response.status_code == 200
#
#


if __name__ == '__main__':
    pytest.main()
