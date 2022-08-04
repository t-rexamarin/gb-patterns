from abc import abstractmethod, ABCMeta


class BaseView:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __call__(self, *args, **kwargs) -> tuple[str, list[bytes]]:
        pass


class PageNotFound404(BaseView):
    def __call__(self, *args, **kwargs) -> tuple[str, list[bytes]]:
        return '404', [b'404 Page Not Found']
