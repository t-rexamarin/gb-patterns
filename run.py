from wsgiref.simple_server import make_server

from homunculus_framework import settings
from homunculus_framework.main import Framework
from urls import routes, fronts


application = Framework(routes=routes, fronts=fronts, settings=settings)

with make_server(host='', port=8080, app=application) as httpd:
    print(f'Starting server {httpd.server_address}...')
    httpd.serve_forever()
