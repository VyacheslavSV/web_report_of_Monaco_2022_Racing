from web_report import web_rep_app


def test_config():
    assert not web_rep_app().testing
    assert web_rep_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'