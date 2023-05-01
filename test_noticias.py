from noticias import archivo_pagina
from unittest import mock


def test_archivo_pagina(mocker):

    content = "<html><head><title>Example</title></head> \
    <body><h1>Example</h1></body></html>"
    mocker.patch('urllib.request.urlopen', return_value=mock.Mock(
        read=lambda: content.encode()))
    respuesta = archivo_pagina(
        'https://www.eltiempo.com', 'bucketnoticias', 'elTiempo-')
    assert respuesta == content
