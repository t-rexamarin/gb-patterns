from os import path

from homunculus_framework.content_types import CONTENT_TYPES_MAP
from homunculus_framework.views import PageNotFound404
from homunculus_framework.utils import ResponseCodes as Response
from homunculus_framework.requests import GetRequest, PostRequest


class Framework:
    def __init__(self, routes, fronts: list, settings):
        self.routes = routes
        self.fronts = fronts
        self.settings = settings

    def __call__(self, environ: dict, start_response):
        _path: str = environ['PATH_INFO']
        request = {}
        request_method: str = environ['REQUEST_METHOD']
        request['method'] = request_method

        if not _path.endswith('/'):
            _path = f'{_path}/'

        if request_method == 'POST':
            post_data = PostRequest().get_request_params(environ)
            request['data'] = post_data
        if request_method == 'GET' and not _path.startswith(self.settings.STATIC_URL):
            request_params = GetRequest().get_query_string(environ)
            request['request_params'] = request_params
            # print(f'Получены get параметры {request_params}')

        if _path in self.routes:
            view = self.routes[_path]
            content_type = self.get_content_type(_path)
            code, body = view(request)
            body = body.encode('utf-8')
        elif _path.startswith(self.settings.STATIC_URL):
            file_path = _path[len(self.settings.STATIC_URL):len(_path) - 1]
            # print(file_path)
            content_type = self.get_content_type(file_path)
            # print(content_type)
            code, body = self.get_static(self.settings.STATIC_FILES_DIR, file_path)
        else:
            view = PageNotFound404()
            content_type = self.get_content_type(_path)
            code, body = view(request)
            body = body.encode('utf-8')

        for front in self.fronts:
            front(request)

        start_response(code, [('Content-Type', content_type)])
        return [body]

    @staticmethod
    def get_static(static_dir, file_path):
        path_to_file = path.join(static_dir, file_path)
        with open(path_to_file, 'rb') as f:
            file_content = f.read()
        status_code = Response.code_200
        return status_code, file_content

    @staticmethod
    def get_content_type(file_path, content_types_map=CONTENT_TYPES_MAP):
        file_name = path.basename(file_path).lower()
        extension = path.splitext(file_name)[1]
        return content_types_map.get(extension, 'text/html')
