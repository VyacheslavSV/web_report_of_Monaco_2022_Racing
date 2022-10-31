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
    response = client.get('/driver/')
    assert response.data == (b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <'
                             b'title></title>\n</head>\n<body>\n\n\n\n<ul>\n\n<li><a href ="/driver/?driver'
                             b'_id=Sebastian+Vettel">S\n\nV\n\nF</a>, Sebastian Vettel </li>\n\n<li><a hr'
                             b'ef ="/driver/?driver_id=Valtteri+Bottas">V\n\nB\n\nM</a>, Valtteri Bottas </'
                             b'li>\n\n<li><a href ="/driver/?driver_id=Stoffel+Vandoorne">S\n\nV\n\nM</a>'
                             b', Stoffel Vandoorne </li>\n\n<li><a href ="/driver/?driver_id=Kimi+Raikkon'
                             b'en">K\n\nR\n\nF</a>, Kimi Raikkonen </li>\n\n<li><a href ="/driver/?driver'
                             b'_id=Fernando+Alonso">F\n\nA\n\nM</a>, Fernando Alonso </li>\n\n<li><a href'
                             b' ="/driver/?driver_id=Charles+Leclerc">C\n\nL\n\nS</a>, Charles Leclerc </li'
                             b'>\n\n<li><a href ="/driver/?driver_id=Sergio+Perez">S\n\nP\n\nF</a>, Sergi'
                             b'o Perez </li>\n\n<li><a href ="/driver/?driver_id=Romain+Grosjean">R\n\n'
                             b'G\n\nH</a>, Romain Grosjean </li>\n\n<li><a href ="/driver/?driver_id=Pierre'
                             b'+Gasly">P\n\nG\n\nS</a>, Pierre Gasly </li>\n\n<li><a href ="/driver/?driv'
                             b'er_id=Carlos+Sainz">C\n\nS\n\nR</a>, Carlos Sainz </li>\n\n<li><a href ="/'
                             b'driver/?driver_id=Nico+Hulkenberg">N\n\nH\n\nR</a>, Nico Hulkenberg </li'
                             b'>\n\n<li><a href ="/driver/?driver_id=Brendon+Hartley">B\n\nH\n\nS</a>, Br'
                             b'endon Hartley </li>\n\n<li><a href ="/driver/?driver_id=Marcus+Ericsson">M'
                             b'\n\nE\n\nS</a>, Marcus Ericsson </li>\n\n<li><a href ="/driver/?driver_id='
                             b'Lance+Stroll">L\n\nS\n\nW</a>, Lance Stroll </li>\n\n<li><a href ="/driver'
                             b'/?driver_id=Kevin+Magnussen">K\n\nM\n\nH</a>, Kevin Magnussen </li>\n\n<li'
                             b'><a href ="/driver/?driver_id=Daniel+Ricciardo">D\n\nR\n\nR</a>, Daniel Ricc'
                             b'iardo </li>\n\n<li><a href ="/driver/?driver_id=Sergey+Sirotkin">S\n\nS\n'
                             b'\nW</a>, Sergey Sirotkin </li>\n\n<li><a href ="/driver/?driver_id=Esteban+'
                             b'Ocon">E\n\nO\n\nF</a>, Esteban Ocon </li>\n\n<li><a href ="/driver/?driver'
                             b'_id=Lewis+Hamilton">L\n\nH\n\nM</a>, Lewis Hamilton </li>\n\n</ul>\n\n\n<'
                             b'/body>\n</html>')


def test_driver_order(client):
    response = client.get('/driver/', query_string={"order": "desc"})
    assert response.data == (b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <'
                             b'title></title>\n</head>\n<body>\n\n\n\n<ul>\n\n<li><a href ="/driver/?driver'
                             b'_id=Lewis+Hamilton">L\n\nH\n\nM</a>, Lewis Hamilton </li>\n\n<li><a href ='
                             b'"/driver/?driver_id=Esteban+Ocon">E\n\nO\n\nF</a>, Esteban Ocon </li>\n\n<'
                             b'li><a href ="/driver/?driver_id=Sergey+Sirotkin">S\n\nS\n\nW</a>, Sergey Sir'
                             b'otkin </li>\n\n<li><a href ="/driver/?driver_id=Daniel+Ricciardo">D\n\nR'
                             b'\n\nR</a>, Daniel Ricciardo </li>\n\n<li><a href ="/driver/?driver_id=Kevin+'
                             b'Magnussen">K\n\nM\n\nH</a>, Kevin Magnussen </li>\n\n<li><a href ="/driver'
                             b'/?driver_id=Lance+Stroll">L\n\nS\n\nW</a>, Lance Stroll </li>\n\n<li><a hr'
                             b'ef ="/driver/?driver_id=Marcus+Ericsson">M\n\nE\n\nS</a>, Marcus Ericsson </'
                             b'li>\n\n<li><a href ="/driver/?driver_id=Brendon+Hartley">B\n\nH\n\nS</a>, '
                             b'Brendon Hartley </li>\n\n<li><a href ="/driver/?driver_id=Nico+Hulkenberg"'
                             b'>N\n\nH\n\nR</a>, Nico Hulkenberg </li>\n\n<li><a href ="/driver/?driver_i'
                             b'd=Carlos+Sainz">C\n\nS\n\nR</a>, Carlos Sainz </li>\n\n<li><a href ="/driv'
                             b'er/?driver_id=Pierre+Gasly">P\n\nG\n\nS</a>, Pierre Gasly </li>\n\n<li><a '
                             b'href ="/driver/?driver_id=Romain+Grosjean">R\n\nG\n\nH</a>, Romain Grosjean '
                             b'</li>\n\n<li><a href ="/driver/?driver_id=Sergio+Perez">S\n\nP\n\nF</a>, S'
                             b'ergio Perez </li>\n\n<li><a href ="/driver/?driver_id=Charles+Leclerc">C\n\n'
                             b'L\n\nS</a>, Charles Leclerc </li>\n\n<li><a href ="/driver/?driver_id=Fernan'
                             b'do+Alonso">F\n\nA\n\nM</a>, Fernando Alonso </li>\n\n<li><a href ="/driver'
                             b'/?driver_id=Kimi+Raikkonen">K\n\nR\n\nF</a>, Kimi Raikkonen </li>\n\n<li><'
                             b'a href ="/driver/?driver_id=Stoffel+Vandoorne">S\n\nV\n\nM</a>, Stoffel Vand'
                             b'oorne </li>\n\n<li><a href ="/driver/?driver_id=Valtteri+Bottas">V\n\nB\n'
                             b'\nM</a>, Valtteri Bottas </li>\n\n<li><a href ="/driver/?driver_id=Sebastia'
                             b'n+Vettel">S\n\nV\n\nF</a>, Sebastian Vettel </li>\n\n</ul>\n\n\n</body>\n<'
                             b'/html>')


def test_driver_driver_id(client):
    response = client.get('/driver/', query_string={'driver_id': 'SVF'})
    assert response.text == ('<!DOCTYPE html>\n'
                             '<html lang="en">\n'
                             '<head>\n'
                             '    <meta charset="UTF-8">\n'
                             '    <title></title>\n'
                             '</head>\n'
                             '<body>\n'
                             '\n'
                             '<b>(&#39;Sebastian Vettel&#39;, &#39;FERRARI&#39;, '
                             '&#39;0:01:04.415000&#39;)</b>\n'
                             '\n'
                             '</body>\n'
                             '</html>')



if __name__ == '__main__':
    pytest.main()
