from homunculus_framework.templator import render
from homunculus_framework.views import BaseView
from homunculus_framework.utils import ResponseCodes as Response


class IndexView(BaseView):
    template_name = 'index.html'
    title = 'Стартовая страница'

    def __call__(self, request: dict):
        request['title'] = self.title
        return Response.code_200, render(template_name=self.template_name, props=request)


class AboutView(BaseView):
    template_name = 'about.html'
    title = 'О сервисе'

    def __call__(self, request, **kwargs):
        request['title'] = self.title
        return Response.code_200, render(template_name=self.template_name, props=request)


class PricingView(BaseView):
    template_name = 'pricing.html'
    title = 'Цены'

    def __call__(self, request, **kwargs):
        request['title'] = self.title
        return Response.code_200, render(template_name=self.template_name, props=request)


class ContactUsView(BaseView):
    template_name = 'contact_us.html'
    title = 'Обратная связь'

    def __call__(self, request, **kwargs):
        if request.get('post_data'):
            request['msg_success'] = True

        request['title'] = self.title
        return Response.code_200, render(template_name=self.template_name, props=request)
