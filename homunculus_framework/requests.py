from urllib.parse import unquote_plus


class BaseRequest:
    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                key, val = item.split('=')
                result[key] = val
        return result


class GetRequest(BaseRequest):
    def get_query_string(self, environ):
        query_string = environ['QUERY_STRING']
        parsed_data = self.parse_input_data(query_string)
        return parsed_data


class PostRequest(BaseRequest):
    @staticmethod
    def get_wsgi_input_data(environ) -> bytes:
        content_length_data = environ.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        # print(type(environ['wsgi.input']))
        # data = environ['wsgi_input'].read(content_length)
        if content_length > 0:
            data = environ['wsgi.input'].read(content_length)
        else:
            data = b''
        # print(data)
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        decoded_data = data.decode('utf-8')
        decoded_data = unquote_plus(decoded_data, 'utf-8')
        result = self.parse_input_data(decoded_data)
        return result

    def get_request_params(self, environ):
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        # print(data)
        return data
