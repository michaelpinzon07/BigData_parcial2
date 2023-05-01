from noticias import archivo_espectador
from datetime import date
import unicodedata

fecha = date.today()


def archivo_espectador(mocker):

    file = "headlines/raw/elEspectador-" + str(fecha.year) + "-" + str(
        fecha.strftime('%m')) + "-" + str(fecha.strftime('%d')) + ".html"
    texto_mock = 'ÁáÉéÍíÓóÚú'
    mocker.patch.object(unicodedata, 'normalize', return_value=texto_mock)
    respuesta = archivo_espectador(file)
    assert respuesta == ''
