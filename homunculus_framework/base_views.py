import abc

from homunculus_framework.templator import render
from homunculus_framework.utils import ResponseCodes as Response


class BaseView(abc.ABC):
    template_name: str = None
    title: str = None

    @abc.abstractmethod
    def __call__(self, *args, **kwargs) -> tuple[str, str]:
        return '', render(template_name=self.template_name, folder='templates', **kwargs)


class PageNotFound404(BaseView):
    template_name = 'page404.html'
    title = 'Страница не найдена'

    def __call__(self, *args, **kwargs):
        return Response.code_404, render(
            template_name=self.template_name,
            folder='homunculus_framework/base_templates',
            **kwargs
        )
