from os import path

from homunculus_framework.content_types import CONTENT_TYPES_MAP
from homunculus_framework.views import PageNotFound404
from homunculus_framework.utils import ResponseCodes as response


class Framework:
    def __init__(self, routes, fronts: list, settings):
        self.routes = routes
        self.fronts = fronts
        self.settings = settings

    def __call__(self, environ: dict, start_response):
        path: str = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        request = {}
        for front in self.fronts:
            front(request)

        if path in self.routes:
            view = self.routes[path]
            content_type = self.get_content_type(path)
            code, body = view(request)
            body = body.encode('utf-8')
        elif path.startswith(self.settings.STATIC_URL):
            file_path = path[len(self.settings.STATIC_URL):len(path) - 1]
            # print(file_path)
            content_type = self.get_content_type(file_path)
            # print(content_type)
            code, body = self.get_static(self.settings.STATIC_FILES_DIR, file_path)
        else:
            view = PageNotFound404()
            content_type = self.get_content_type(path)
            code, body = view(request)
            body = body.encode('utf-8')

        # code, body = view(request)
        start_response(code, [('Content-Type', content_type)])
        return [body]

    @staticmethod
    def get_static(static_dir, file_path):
        path_to_file = path.join(static_dir, file_path)
        with open(path_to_file, 'rb') as f:
            file_content = f.read()
        status_code = response.code_200
        return status_code, file_content

    @staticmethod
    def get_content_type(file_path, content_types_map=CONTENT_TYPES_MAP):
        file_name = path.basename(file_path).lower()
        extension = path.splitext(file_name)[1]
        return content_types_map.get(extension, 'text/html')
