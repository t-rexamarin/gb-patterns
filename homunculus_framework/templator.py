import os

from jinja2 import Template, Environment, FileSystemLoader


def render(template_name: str, folder: str = 'templates', static_url: str = '/static/', **kwargs):
    """

    :param template_name:
    :param folder:
    :param static_url:
    :param kwargs:
    :return:
    """
    # path = os.path.dirname(__file__)
    env = Environment()
    env.loader = FileSystemLoader(folder)
    env.globals['static'] = static_url
    template = env.get_template(template_name)
    # file_path = os.path.join(folder, template_name)
    # with open(file_path, encoding='utf-8') as f:
    #     template = Template(f.read())
    return template.render(**kwargs)
