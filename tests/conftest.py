import pytest

from web_report import web_rep_app

@pytest.fixture
def app():
    app = web_rep_app()
    return app
