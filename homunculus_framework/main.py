from typing import List, Any, Dict

from homunculus_framework.views import PageNotFound404


class Framework:
    def __init__(self, routes: Dict[Any], fronts: list):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ: dict, start_response):
        path = environ['PATH_INFO']
        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404
        request = {}
        for front in self.fronts:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body
