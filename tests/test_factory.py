import pytest

from web_report import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_report(client):
    response = client.get('/report/')
    assert response.data == (b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <'
                             b'title></title>\n</head>\n<body>\n<ul>\n\n<li>Sebastian Vettel, FERRARI, 0'
                             b':01:04.415000</li>\n\n<li>Valtteri Bottas, MERCEDES, 0:01:12.434000</li>\n\n'
                             b'<li>Stoffel Vandoorne, MCLAREN RENAULT, 0:01:12.463000</li>\n\n<li>Kimi Ra'
                             b'ikkonen, FERRARI, 0:01:12.639000</li>\n\n<li>Fernando Alonso, MCLAREN RENA'
                             b'ULT, 0:01:12.657000</li>\n\n<li>Charles Leclerc, SAUBER FERRARI, 0:01:12.8'
                             b'29000</li>\n\n<li>Sergio Perez, FORCE INDIA MERCEDES, 0:01:12.848000</li>\n'
                             b'\n<li>Romain Grosjean, HAAS FERRARI, 0:01:12.930000</li>\n\n<li>Pierre Gasl'
                             b'y, SCUDERIA TORO ROSSO HONDA, 0:01:12.941000</li>\n\n<li>Carlos Sainz, REN'
                             b'AULT, 0:01:12.950000</li>\n\n<li>Nico Hulkenberg, RENAULT, 0:01:13.065000<'
                             b'/li>\n\n<li>Brendon Hartley, SCUDERIA TORO ROSSO HONDA, 0:01:13.179000</li'
                             b'>\n\n<li>Marcus Ericsson, SAUBER FERRARI, 0:01:13.265000</li>\n\n<li>Lance S'
                             b'troll, WILLIAMS MERCEDES, 0:01:13.323000</li>\n\n<li>Kevin Magnussen, HAAS'
                             b' FERRARI, 0:01:13.393000</li>\n\n<li>Daniel Ricciardo, RED BULL RACING TAG'
                             b' HEUER, 0:02:47.987000</li>\n\n<li>Sergey Sirotkin, WILLIAMS MERCEDES, 0:0'
                             b'4:47.294000</li>\n\n<li>Esteban Ocon, FORCE INDIA MERCEDES, 0:05:46.972000'
                             b'</li>\n\n<li>Lewis Hamilton, MERCEDES, 0:06:47.540000</li>\n\n</ul>\n</bo'
                             b'dy>\n</html>')


def test_report_order(client):
    response = client.get('/report/', query_string={"order": "desc"})
    assert response.data == (b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <'
                             b'title></title>\n</head>\n<body>\n<ul>\n\n<li>Lewis Hamilton, MERCEDES, 0:'
                             b'06:47.540000</li>\n\n<li>Esteban Ocon, FORCE INDIA MERCEDES, 0:05:46.97200'
                             b'0</li>\n\n<li>Sergey Sirotkin, WILLIAMS MERCEDES, 0:04:47.294000</li>\n\n<li'
                             b'>Daniel Ricciardo, RED BULL RACING TAG HEUER, 0:02:47.987000</li>\n\n<li>K'
                             b'evin Magnussen, HAAS FERRARI, 0:01:13.393000</li>\n\n<li>Lance Stroll, WIL'
                             b'LIAMS MERCEDES, 0:01:13.323000</li>\n\n<li>Marcus Ericsson, SAUBER FERRARI'
                             b', 0:01:13.265000</li>\n\n<li>Brendon Hartley, SCUDERIA TORO ROSSO HONDA, 0'
                             b':01:13.179000</li>\n\n<li>Nico Hulkenberg, RENAULT, 0:01:13.065000</li>\n\n<'
                             b'li>Carlos Sainz, RENAULT, 0:01:12.950000</li>\n\n<li>Pierre Gasly, SCUDERI'
                             b'A TORO ROSSO HONDA, 0:01:12.941000</li>\n\n<li>Romain Grosjean, HAAS FERRA'
                             b'RI, 0:01:12.930000</li>\n\n<li>Sergio Perez, FORCE INDIA MERCEDES, 0:01:12'
                             b'.848000</li>\n\n<li>Charles Leclerc, SAUBER FERRARI, 0:01:12.829000</li>\n\n'
                             b'<li>Fernando Alonso, MCLAREN RENAULT, 0:01:12.657000</li>\n\n<li>Kimi Raik'
                             b'konen, FERRARI, 0:01:12.639000</li>\n\n<li>Stoffel Vandoorne, MCLAREN RENA'
                             b'ULT, 0:01:12.463000</li>\n\n<li>Valtteri Bottas, MERCEDES, 0:01:12.434000<'
                             b'/li>\n\n<li>Sebastian Vettel, FERRARI, 0:01:04.415000</li>\n\n</ul>\n</bo'
                             b'dy>\n</html>')


def test_driver(client):
    response = client.get('/report/')
    assert response.data == (b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <'
                             b'title></title>\n</head>\n<body>\n<ul>\n\n<li>Sebastian Vettel, FERRARI, 0'
                             b':01:04.415000</li>\n\n<li>Valtteri Bottas, MERCEDES, 0:01:12.434000</li>\n\n'
                             b'<li>Stoffel Vandoorne, MCLAREN RENAULT, 0:01:12.463000</li>\n\n<li>Kimi Ra'
                             b'ikkonen, FERRARI, 0:01:12.639000</li>\n\n<li>Fernando Alonso, MCLAREN RENA'
                             b'ULT, 0:01:12.657000</li>\n\n<li>Charles Leclerc, SAUBER FERRARI, 0:01:12.8'
                             b'29000</li>\n\n<li>Sergio Perez, FORCE INDIA MERCEDES, 0:01:12.848000</li>\n'
                             b'\n<li>Romain Grosjean, HAAS FERRARI, 0:01:12.930000</li>\n\n<li>Pierre Gasl'
                             b'y, SCUDERIA TORO ROSSO HONDA, 0:01:12.941000</li>\n\n<li>Carlos Sainz, REN'
                             b'AULT, 0:01:12.950000</li>\n\n<li>Nico Hulkenberg, RENAULT, 0:01:13.065000<'
                             b'/li>\n\n<li>Brendon Hartley, SCUDERIA TORO ROSSO HONDA, 0:01:13.179000</li'
                             b'>\n\n<li>Marcus Ericsson, SAUBER FERRARI, 0:01:13.265000</li>\n\n<li>Lance S'
                             b'troll, WILLIAMS MERCEDES, 0:01:13.323000</li>\n\n<li>Kevin Magnussen, HAAS'
                             b' FERRARI, 0:01:13.393000</li>\n\n<li>Daniel Ricciardo, RED BULL RACING TAG'
                             b' HEUER, 0:02:47.987000</li>\n\n<li>Sergey Sirotkin, WILLIAMS MERCEDES, 0:0'
                             b'4:47.294000</li>\n\n<li>Esteban Ocon, FORCE INDIA MERCEDES, 0:05:46.972000'
                             b'</li>\n\n<li>Lewis Hamilton, MERCEDES, 0:06:47.540000</li>\n\n</ul>\n</bo'
                             b'dy>\n</html>')


def test_driver_order(client):
    response = client.get('/report/', query_string={"order": "desc"})
    assert response.data == (b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <'
                             b'title></title>\n</head>\n<body>\n<ul>\n\n<li>Lewis Hamilton, MERCEDES, 0:'
                             b'06:47.540000</li>\n\n<li>Esteban Ocon, FORCE INDIA MERCEDES, 0:05:46.97200'
                             b'0</li>\n\n<li>Sergey Sirotkin, WILLIAMS MERCEDES, 0:04:47.294000</li>\n\n<li'
                             b'>Daniel Ricciardo, RED BULL RACING TAG HEUER, 0:02:47.987000</li>\n\n<li>K'
                             b'evin Magnussen, HAAS FERRARI, 0:01:13.393000</li>\n\n<li>Lance Stroll, WIL'
                             b'LIAMS MERCEDES, 0:01:13.323000</li>\n\n<li>Marcus Ericsson, SAUBER FERRARI'
                             b', 0:01:13.265000</li>\n\n<li>Brendon Hartley, SCUDERIA TORO ROSSO HONDA, 0'
                             b':01:13.179000</li>\n\n<li>Nico Hulkenberg, RENAULT, 0:01:13.065000</li>\n\n<'
                             b'li>Carlos Sainz, RENAULT, 0:01:12.950000</li>\n\n<li>Pierre Gasly, SCUDERI'
                             b'A TORO ROSSO HONDA, 0:01:12.941000</li>\n\n<li>Romain Grosjean, HAAS FERRA'
                             b'RI, 0:01:12.930000</li>\n\n<li>Sergio Perez, FORCE INDIA MERCEDES, 0:01:12'
                             b'.848000</li>\n\n<li>Charles Leclerc, SAUBER FERRARI, 0:01:12.829000</li>\n\n'
                             b'<li>Fernando Alonso, MCLAREN RENAULT, 0:01:12.657000</li>\n\n<li>Kimi Raik'
                             b'konen, FERRARI, 0:01:12.639000</li>\n\n<li>Stoffel Vandoorne, MCLAREN RENA'
                             b'ULT, 0:01:12.463000</li>\n\n<li>Valtteri Bottas, MERCEDES, 0:01:12.434000<'
                             b'/li>\n\n<li>Sebastian Vettel, FERRARI, 0:01:04.415000</li>\n\n</ul>\n</bo'
                             b'dy>\n</html>')


def test_driver_driver_id(client):
    response = client.post('/report/', query_string={'driver_id': 'SVF'})
    assert response.get_data() == 'Sebastian Vettel, FERRARI, 0:01:04.415000'
    # Проблема, виводить список замість вірного результату, я щось пишу не вірно?
if __name__ == '__main__':
    pytest.main()
