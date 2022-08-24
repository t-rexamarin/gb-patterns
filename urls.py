from front_controllers.base_fc import current_date
from views import *

routes = {
    '/': IndexView(),
    '/about/': AboutView(),
    '/contact_us/': ContactUsView(),
    '/pricing/': PricingView(),
    '/create_category/': CategoryCreateView(),
    '/list_categories/': CategoryListView(),
    '/create_course/': CourseCreateView(),
    '/list_courses/': CourseListView(),
    '/copy_course/': CourseCopyView()
}

fronts = (current_date, )
