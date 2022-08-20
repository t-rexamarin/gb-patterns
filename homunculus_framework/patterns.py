class Category:
    _id = 0

    def __init__(self, name):
        self.id = Category._id
        Category._id += 1
        self.name = name


class Engine:
    def __init__(self):
        self.categories = []

    @staticmethod
    def create_category(name):
        return Category(name=name)