from homunculus_framework.patterns import Engine
from homunculus_framework.templator import render
from homunculus_framework.views import BaseView
from homunculus_framework.utils import ResponseCodes as Response


site = Engine()


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
    courses = {
        'programming': {
            'id': 1,
            'name': 'Программирование',
            'description': 'Супер-пупер курс по программированию от первой женщины программиста.',
            'price': 20000,
            'teacher': 'Ада Лавлейс'
        },
        'painting': {
            'id': 2,
            'name': 'Рисование',
            'description': 'Учимся использовать кисти с мастером своего дела.',
            'price': 15000,
            'teacher': 'Боб Росс'
        },
        'physics': {
            'id': 3,
            'name': 'Физика',
            'description': 'Познаем таинственную природу происходящих вокруг процессов.',
            'price': 15000,
            'teacher': 'Альберт Франкенштейн'
        }
    }

    def __call__(self, request, **kwargs):
        request['title'] = self.title
        request['courses'] = self.courses
        return Response.code_200, render(template_name=self.template_name, props=request)


class ContactUsView(BaseView):
    template_name = 'contact_us.html'
    title = 'Обратная связь'

    def __call__(self, request, **kwargs):
        if request.get('post_data'):
            request['msg_success'] = True

        request['title'] = self.title
        return Response.code_200, render(template_name=self.template_name, props=request)


class CreateCategoryView(BaseView):
    template_name = 'create_category.html'
    title = 'Создание категории'

    def __call__(self, request, **kwargs):
        request['title'] = self.title

        if request['method'] == 'POST':
            data = request['data']
            category_name = data['categoryName']
            print(category_name)

            return Response.code_200, render(template_name=self.template_name, props=request)
        else:
            return Response.code_200, render(template_name=self.template_name, props=request)
