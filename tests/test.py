import pytest
from web_report import drivers_cod_name_dict, fine, report, drivers, page, result

x = [('Sebastian Vettel', 'FERRARI', '0:01:04.415000'), ('Valtteri Bottas', 'MERCEDES', '0:01:12.434000'),
     ('Stoffel Vandoorne', 'MCLAREN RENAULT', '0:01:12.463000'), ('Kimi Raikkonen', 'FERRARI', '0:01:12.639000'),
     ('Fernando Alonso', 'MCLAREN RENAULT', '0:01:12.657000'), ('Charles Leclerc', 'SAUBER FERRARI', '0:01:12.829000'),
     ('Sergio Perez', 'FORCE INDIA MERCEDES', '0:01:12.848000'), ('Romain Grosjean', 'HAAS FERRARI', '0:01:12.930000'),
     ('Pierre Gasly', 'SCUDERIA TORO ROSSO HONDA', '0:01:12.941000'), ('Carlos Sainz', 'RENAULT', '0:01:12.950000'),
     ('Nico Hulkenberg', 'RENAULT', '0:01:13.065000'),
     ('Brendon Hartley', 'SCUDERIA TORO ROSSO HONDA', '0:01:13.179000'),
     ('Marcus Ericsson', 'SAUBER FERRARI', '0:01:13.265000'), ('Lance Stroll', 'WILLIAMS MERCEDES', '0:01:13.323000'),
     ('Kevin Magnussen', 'HAAS FERRARI', '0:01:13.393000'),
     ('Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '0:02:47.987000'),
     ('Sergey Sirotkin', 'WILLIAMS MERCEDES', '0:04:47.294000'),
     ('Esteban Ocon', 'FORCE INDIA MERCEDES', '0:05:46.972000'), ('Lewis Hamilton', 'MERCEDES', '0:06:47.540000')]

y = [{'driver_id': 'SVF', 'name': 'Sebastian Vettel', 'SVF': 'Sebastian Vettel, FERRARI, 0:01:04.415000'},
     {'driver_id': 'VBM', 'name': 'Valtteri Bottas', 'VBM': 'Valtteri Bottas, MERCEDES, 0:01:12.434000'},
     {'driver_id': 'SVM', 'name': 'Stoffel Vandoorne', 'SVM': 'Stoffel Vandoorne, MCLAREN RENAULT, 0:01:12.463000'},
     {'driver_id': 'KRF', 'name': 'Kimi Raikkonen', 'KRF': 'Kimi Raikkonen, FERRARI, 0:01:12.639000'},
     {'driver_id': 'FAM', 'name': 'Fernando Alonso', 'FAM': 'Fernando Alonso, MCLAREN RENAULT, 0:01:12.657000'},
     {'driver_id': 'CLS', 'name': 'Charles Leclerc', 'CLS': 'Charles Leclerc, SAUBER FERRARI, 0:01:12.829000'},
     {'driver_id': 'SPF', 'name': 'Sergio Perez', 'SPF': 'Sergio Perez, FORCE INDIA MERCEDES, 0:01:12.848000'},
     {'driver_id': 'RGH', 'name': 'Romain Grosjean', 'RGH': 'Romain Grosjean, HAAS FERRARI, 0:01:12.930000'},
     {'driver_id': 'PGS', 'name': 'Pierre Gasly', 'PGS': 'Pierre Gasly, SCUDERIA TORO ROSSO HONDA, 0:01:12.941000'},
     {'driver_id': 'CSR', 'name': 'Carlos Sainz', 'CSR': 'Carlos Sainz, RENAULT, 0:01:12.950000'},
     {'driver_id': 'NHR', 'name': 'Nico Hulkenberg', 'NHR': 'Nico Hulkenberg, RENAULT, 0:01:13.065000'},
     {'driver_id': 'BHS', 'name': 'Brendon Hartley',
      'BHS': 'Brendon Hartley, SCUDERIA TORO ROSSO HONDA, 0:01:13.179000'},
     {'driver_id': 'MES', 'name': 'Marcus Ericsson', 'MES': 'Marcus Ericsson, SAUBER FERRARI, 0:01:13.265000'},
     {'driver_id': 'LSW', 'name': 'Lance Stroll', 'LSW': 'Lance Stroll, WILLIAMS MERCEDES, 0:01:13.323000'},
     {'driver_id': 'KMH', 'name': 'Kevin Magnussen', 'KMH': 'Kevin Magnussen, HAAS FERRARI, 0:01:13.393000'},
     {'driver_id': 'DRR', 'name': 'Daniel Ricciardo',
      'DRR': 'Daniel Ricciardo, RED BULL RACING TAG HEUER, 0:02:47.987000'},
     {'driver_id': 'SSW', 'name': 'Sergey Sirotkin', 'SSW': 'Sergey Sirotkin, WILLIAMS MERCEDES, 0:04:47.294000'},
     {'driver_id': 'EOF', 'name': 'Esteban Ocon', 'EOF': 'Esteban Ocon, FORCE INDIA MERCEDES, 0:05:46.972000'},
     {'driver_id': 'LHM', 'name': 'Lewis Hamilton', 'LHM': 'Lewis Hamilton, MERCEDES, 0:06:47.540000'}]


def test_drivers_cod_name_dict():
    assert drivers_cod_name_dict(x) == y


def test_fine():
    assert fine('MES') == 'Marcus Ericsson, SAUBER FERRARI, 0:01:13.265000'


def test_report(client):
    response = client.get('/report')
    assert response.result


if __name__ == '__main__':
    pytest.main()
