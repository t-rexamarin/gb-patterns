


class IndexView(BaseView):
    def __call__(self, request: dict) -> tuple[str, list[bytes]]:
        return '200 OK', [b'<h1>index page</h1>']
