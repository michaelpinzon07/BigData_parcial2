import boto3
import urllib.request
import datetime


def archivo_pagina(url, bucket, nombre):

    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    today = datetime.date.today().strftime('%Y-%m-%d')
    s3 = boto3.resource('s3')
    s3.Object(bucket, 'headlines/raw/{}{}.html'.format(
        nombre, today)).put(Body=content)
    return content


archivo_pagina('https://www.eltiempo.com', 'bucketnoticias', 'elTiempo-')
archivo_pagina('https://www.elespectador.com', 'bucketnoticias', 'elEspectador-')
