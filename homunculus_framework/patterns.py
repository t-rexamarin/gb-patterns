import copy

from typing import Tuple, List


class Category:
    _id: int = 0
    name: str
    courses: list

    def __init__(self, name: str):
        self.id = Category._id
        Category._id += 1
        self.name = name
        self.courses = []


class CourseBase:
    def clone(self):
        return copy.deepcopy(self)


class Course(CourseBase):
    name: str
    category: Category
    location: str

    def __init__(self, name: str, category: Category, location: str):
        self.name = name
        self.category = category
        self.category.courses.append(self)
        self.location = location


class InteractiveCourse(Course):
    pass


class OnlineCourse(Course):
    pass


class CourseFactory:
    types = {
        'interactive': InteractiveCourse,
        'online': OnlineCourse
    }

    @classmethod
    def create(cls, type_, name, category, location) -> [InteractiveCourse, OnlineCourse]:
        return cls.types[type_](name, category, location)


class Engine:
    categories: list
    courses: list

    def __init__(self):
        self.categories = []
        self.courses = []
        self.categories, self.courses = self.fill_data()

    @staticmethod
    def create_category(name: str) -> Category:
        """
        Создание категории.
        """
        return Category(name=name)

    def find_category_by_id(self, cat_id: int) -> str:
        """
        Поиск категории по id.
        """
        for item in self.categories:
            if item.id == cat_id:
                return item
        raise Exception(f'Нет категории с id = {cat_id}')

    @staticmethod
    def create_course(type_: str, name: str, category: str, location: str):
        """
        Создание курса.
        """
        return CourseFactory.create(type_, name, category, location)

    def get_course(self, course_name: str):
        for item in self.courses:
            if item.name == course_name:
                return item
        raise Exception(f'Нет курса с name = {course_name}')

    @staticmethod
    def fill_data() -> Tuple[List[Category], List[Course]]:
        """
        Метод для заполнения тестовыми данными.
        """
        categories_list = []
        courses_list = []

        for i in range(1, 6):
            categories_list.append(Category(name=f'Категория {i}'))

        for i in range(1, 6):
            courses_list.append(Course(
                name=f'Курс {i}',
                category=categories_list[i - 1],
                location=f'Место {i}'
            ))

        return categories_list, courses_list
