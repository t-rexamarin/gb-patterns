from homunculus_framework.patterns import Engine, CourseFactory
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


class CategoryCreateView(BaseView):
    template_name = 'create_category.html'
    title = 'Создание категории'

    def __call__(self, request, **kwargs):
        request['title'] = self.title

        if request['method'] == 'POST':
            data = request['data']
            category_name = data['categoryName']
            category = site.create_category(name=category_name)
            site.categories.append(category)
            self.template_name = 'list_categories.html'

        categories = site.categories
        request['categories'] = categories
        return Response.code_200, render(template_name=self.template_name, props=request)


class CategoryListView(BaseView):
    template_name = 'list_categories.html'
    title = 'Категории курсов'

    def __call__(self, request, **kwargs):
        categories = site.categories
        request['categories'] = categories
        return Response.code_200, render(template_name=self.template_name, props=request)


class CourseCreateView(BaseView):
    template_name = 'create_course.html'
    title = 'Создание курса'

    def __call__(self, request, **kwargs):
        request['title'] = self.title

        if request['method'] == 'POST':
            data = request['data']
            course_category = data['courseCategory']
            course_name = data['courseName']
            course_type = data['courseType']
            course_place = data['coursePlace']
            category = site.find_category_by_id(int(course_category))
            course = site.create_course(type_=course_type, name=course_name, category=category, location=course_place)
            site.courses.append(course)
            self.template_name = 'list_courses.html'

        courses = site.courses
        request['courses'] = courses
        categories = site.categories
        request['categories'] = categories
        course_types = CourseFactory.types
        request['courseTypes'] = course_types
        return Response.code_200, render(template_name=self.template_name, props=request)


class CourseCopyView(BaseView):
    template_name = 'list_courses.html'

    def __call__(self, request, **kwargs):
        data = request['data']
        course_name = data['courseName']
        course = site.get_course(course_name)

        if course:
            new_course = course.clone()
            new_course.name += '_copy'
            site.courses.append(new_course)

        courses = site.courses
        request['courses'] = courses
        return Response.code_200, render(template_name=self.template_name, props=request)


class CourseListView(BaseView):
    template_name = 'list_courses.html'
    title = 'Список курсов'

    def __call__(self, request, **kwargs):
        courses = site.courses
        request['courses'] = courses
        return Response.code_200, render(template_name=self.template_name, props=request)
